# Generated by Django 3.2.11 on 2022-01-19 12:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='pic_url',
            field=models.URLField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
