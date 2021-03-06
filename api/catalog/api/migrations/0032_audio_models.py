# Generated by Django 2.2.16 on 2021-06-28 06:29

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0031_auto_20210604_1825'),
    ]

    operations = [
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('identifier', models.UUIDField(db_index=True, help_text='Our unique identifier for an open-licensed work.', unique=True)),
                ('foreign_identifier', models.CharField(blank=True, db_index=True, help_text='The identifier provided by the upstream source.', max_length=1000, null=True, unique=True)),
                ('title', models.CharField(blank=True, max_length=2000, null=True)),
                ('foreign_landing_url', models.CharField(blank=True, help_text='The landing page of the work.', max_length=1000, null=True)),
                ('creator', models.CharField(blank=True, max_length=2000, null=True)),
                ('creator_url', models.URLField(blank=True, max_length=2000, null=True)),
                ('url', models.URLField(help_text='The actual URL to the media file.', max_length=1000, unique=True)),
                ('filesize', models.IntegerField(blank=True, null=True)),
                ('watermarked', models.NullBooleanField()),
                ('license', models.CharField(max_length=50)),
                ('license_version', models.CharField(blank=True, max_length=25, null=True)),
                ('provider', models.CharField(blank=True, db_index=True, help_text='The content provider, e.g. Flickr, Jamendo...', max_length=80, null=True)),
                ('source', models.CharField(blank=True, db_index=True, help_text='The source of the data, meaning a particular dataset. Source and provider can be different. Eg: the Google Open Images dataset is source=openimages, but provider=flickr.', max_length=80, null=True)),
                ('last_synced_with_source', models.DateTimeField(blank=True, db_index=True, null=True)),
                ('removed_from_source', models.BooleanField(default=False)),
                ('view_count', models.IntegerField(default=0)),
                ('tags', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('tags_list', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), blank=True, null=True, size=None)),
                ('meta_data', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('audio_set_position', models.IntegerField(blank=True, help_text='Ordering of the audio in the set.', null=True)),
                ('genres', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=80), db_index=True, help_text='The artistic style of this audio file, eg. hip-hop (music) / tech (podcasts).', null=True, size=None)),
                ('category', models.CharField(blank=True, db_index=True, help_text='The category of this audio file, eg. music, sound_effect, podcast, news & audiobook.', max_length=80, null=True)),
                ('duration', models.IntegerField(blank=True, help_text='The time length of the audio file in milliseconds.', null=True)),
                ('bit_rate', models.IntegerField(blank=True, help_text='Number in bits per second, eg. 128000.', null=True)),
                ('sample_rate', models.IntegerField(blank=True, help_text='Number in hertz, eg. 44100.', null=True)),
                ('alt_files', django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='JSON describing alternative files for this audio.', null=True)),
            ],
            options={
                'db_table': 'audio',
            },
        ),
        migrations.CreateModel(
            name='AudioReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('identifier', models.UUIDField(help_text='The ID for media to be reported.')),
                ('reason', models.CharField(choices=[('mature', 'mature'), ('dmca', 'dmca'), ('other', 'other')], help_text='The reason to report media to fauxpenverse.', max_length=20)),
                ('description', models.TextField(blank=True, help_text='The explanation on why media is being reported.', max_length=500, null=True)),
                ('status', models.CharField(choices=[('pending_review', 'pending_review'), ('mature_filtered', 'mature_filtered'), ('deindexed', 'deindexed'), ('no_action', 'no_action')], default='pending_review', max_length=20)),
            ],
            options={
                'db_table': 'nsfw_reports_audio',
            },
        ),
        migrations.CreateModel(
            name='AudioSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('identifier', models.UUIDField(db_index=True, help_text='Our unique identifier for an open-licensed work.', unique=True)),
                ('foreign_identifier', models.CharField(blank=True, db_index=True, help_text='The identifier provided by the upstream source.', max_length=1000, null=True, unique=True)),
                ('title', models.CharField(blank=True, max_length=2000, null=True)),
                ('foreign_landing_url', models.CharField(blank=True, help_text='The landing page of the work.', max_length=1000, null=True)),
                ('creator', models.CharField(blank=True, max_length=2000, null=True)),
                ('creator_url', models.URLField(blank=True, max_length=2000, null=True)),
                ('url', models.URLField(help_text='The actual URL to the media file.', max_length=1000, unique=True)),
                ('filesize', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DeletedAudio',
            fields=[
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('identifier', models.UUIDField(help_text='The identifier of the deleted media.', primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MatureAudio',
            fields=[
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('identifier', models.UUIDField(primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AudioList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(help_text='Display name', max_length=2000)),
                ('slug', models.CharField(db_index=True, help_text='A unique identifier used to make a friendly URL for downstream API consumers.', max_length=200, unique=True)),
                ('auth', models.CharField(help_text='A randomly generated string assigned upon list creation. Used to authenticate updates and deletions.', max_length=64)),
                ('audios', models.ManyToManyField(help_text='A list of identifier keys corresponding to audios.', related_name='lists', to='api.Audio')),
            ],
            options={
                'db_table': 'audiolist',
            },
        ),
        migrations.AddField(
            model_name='audio',
            name='audio_set',
            field=models.ForeignKey(blank=True, help_text='Reference to set of which this track is a part.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.AudioSet'),
        ),
    ]
