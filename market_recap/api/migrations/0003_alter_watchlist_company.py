# Generated by Django 3.2.9 on 2021-12-03 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_watchlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlist',
            name='company',
            field=models.CharField(default='', max_length=126),
        ),
    ]