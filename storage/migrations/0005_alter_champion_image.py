# Generated by Django 4.0.3 on 2022-04-07 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0004_champion_image_champion_name_champion_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='champion',
            name='image',
            field=models.URLField(default=''),
        ),
    ]