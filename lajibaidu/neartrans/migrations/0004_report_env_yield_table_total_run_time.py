# Generated by Django 3.1 on 2020-02-19 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neartrans', '0003_auto_20200219_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='report_env_yield_table',
            name='total_run_time',
            field=models.IntegerField(default=0),
        ),
    ]