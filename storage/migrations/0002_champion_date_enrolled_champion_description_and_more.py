# Generated by Django 4.0.3 on 2022-04-07 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='champion',
            name='date_enrolled',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='champion',
            name='description',
            field=models.TextField(default='this is description'),
        ),
        migrations.AddField(
            model_name='champion',
            name='name',
            field=models.CharField(default='Aatrox', max_length=50),
        ),
        migrations.AddField(
            model_name='champion',
            name='race',
            field=models.CharField(default='Human', max_length=50),
        ),
        migrations.AddField(
            model_name='champion',
            name='region',
            field=models.CharField(default='Aatrox', max_length=50),
        ),
        migrations.AddField(
            model_name='champion',
            name='role',
            field=models.CharField(default='Aatrox', max_length=50),
        ),
    ]
