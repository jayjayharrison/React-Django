# Generated by Django 3.2.9 on 2021-12-03 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_watchlist_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlist',
            name='ticker',
            field=models.CharField(default='', max_length=5),
        ),
    ]
