# Generated by Django 3.2.9 on 2021-12-03 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_watchlist_ticker'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watchlist',
            name='company',
        ),
        migrations.AlterField(
            model_name='watchlist',
            name='ticker',
            field=models.CharField(default='', max_length=5, unique=True),
        ),
    ]
