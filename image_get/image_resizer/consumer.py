import settings
import logging as log
import asyncio
import aiohttp
import datetime as dt
from functools import partial
from pykafka import KafkaClient
from io import BytesIO
from PIL import Image


def kafka_connect():
    client = KafkaClient(hosts=settings.KAFKA_HOSTS)
    return client


def _parse_message(message):
    log.debug(f'Received {message}')
    return str(message.value, 'utf-8')


async def poll_consumer(consumer, batch_size):
    """
    Poll the Kafka consumer for a batch of messages and parse them.
    :param consumer:
    :param batch_size: The number of events to return from the queue.
    :return:
    """
    batch = []
    # Track how much time has passed since the last message arrived.
    # If too much time passes, we don't need to keep waiting for a full batch.
    last_iteration = dt.datetime.now()
    max_wait = 3
    for idx, message in enumerate(consumer):
        parsed = _parse_message(message)
        batch.append(parsed)
        elapsed_time = dt.datetime.now() - last_iteration
        if idx >= batch_size or elapsed_time.total_seconds() > max_wait:
            break
    return batch


async def consume(kafka_topic):
    """
    Listen for inbound image URLs.
    :return:
    """
    consumer = kafka_topic.get_balanced_consumer(
        consumer_group='image_spiders',
        auto_commit_enable=True,
        zookeeper_connect=settings.ZOOKEEPER_HOST
    )
    session = aiohttp.ClientSession()
    while True:
        messages = await poll_consumer(consumer, settings.BATCH_SIZE)
        # Schedule resizing tasks
        tasks = []
        for msg in messages:
            tasks.append(process_image(session, msg))
        await asyncio.gather(*tasks)


def thumbnail_image(img: Image):
    img.thumbnail(size=settings.TARGET_RESOLUTION, resample=Image.NEAREST)
    log.debug('Resized image')


async def process_image(session, url):
    """Get an image, resize it, and upload it to S3."""
    loop = asyncio.get_event_loop()
    img_resp = await session.get(url)
    buffer = BytesIO(await img_resp.read())
    img = Image.open(buffer)
    await loop.run_in_executor(None, partial(thumbnail_image, img))


if __name__ == '__main__':
    log.basicConfig(level=log.DEBUG)
    kafka_client = kafka_connect()
    inbound_images = kafka_client.topics['inbound_images']
    loop = asyncio.get_event_loop()
    loop.run_until_complete(consume(kafka_topic=inbound_images))

