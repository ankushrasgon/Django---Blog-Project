# Generated by Django 2.1.7 on 2019-04-18 15:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('database_app', '0002_auto_20190418_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 18, 15, 6, 10, 133933, tzinfo=utc)),
        ),
    ]