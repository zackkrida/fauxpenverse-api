# Generated by Django 2.2.10 on 2020-04-23 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0022_reportimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='MatureImages',
            fields=[
                ('identifier', models.UUIDField(primary_key=True, serialize=False, unique=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='deletedimages',
            name='deleted_id',
        ),
        migrations.RemoveField(
            model_name='deletedimages',
            name='deleting_user',
        ),
        migrations.RemoveField(
            model_name='deletedimages',
            name='id',
        ),
        migrations.AddField(
            model_name='deletedimages',
            name='identifier',
            field=models.UUIDField(default='c9341bce-6e8b-4d6a-b098-29f5ca1253ac', help_text='The identifier of the deleted image.', primary_key=True, serialize=False, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='imagereport',
            name='status',
            field=models.CharField(choices=[('pending', 'pending'), ('confirmed', 'confirmed'), ('rejected', 'rejected')], default='pending', max_length=20),
        ),
        migrations.AlterField(
            model_name='imagereport',
            name='description',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='imagereport',
            name='reason',
            field=models.CharField(choices=[('mature', 'mature'), ('dmca', 'dmca'), ('other', 'other')], max_length=20),
        ),
    ]