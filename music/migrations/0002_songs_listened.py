# Generated by Django 5.0.4 on 2024-05-11 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='songs',
            name='listened',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]
