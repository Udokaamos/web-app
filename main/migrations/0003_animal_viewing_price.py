# Generated by Django 3.2.11 on 2022-01-19 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_animal_pic_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='viewing_price',
            field=models.FloatField(default=0),
        ),
    ]
