# Generated by Django 3.1 on 2020-02-21 15:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('neartrans', '0002_auto_20200221_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report_record_by_test_tool_table',
            name='record_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 21, 15, 10, 51, 653259, tzinfo=utc)),
        ),
    ]
