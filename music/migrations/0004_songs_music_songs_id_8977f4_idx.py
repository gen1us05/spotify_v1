# Generated by Django 5.0.4 on 2024-05-11 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_alter_songs_options'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='songs',
            index=models.Index(fields=['id'], name='music_songs_id_8977f4_idx'),
        ),
    ]
