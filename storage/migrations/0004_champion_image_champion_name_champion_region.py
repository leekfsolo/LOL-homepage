# Generated by Django 4.0.3 on 2022-04-07 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0003_remove_champion_date_enrolled_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='champion',
            name='image',
            field=models.URLField(default='', max_length=255, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='champion',
            name='name',
            field=models.CharField(default='Aatrox', max_length=50),
        ),
        migrations.AddField(
            model_name='champion',
            name='region',
            field=models.CharField(default='Runeterra', max_length=50),
        ),
    ]
