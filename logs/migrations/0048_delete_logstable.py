# Generated by Django 4.1.7 on 2023-03-23 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0047_remove_logstable_logs_logstable_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='LogsTable',
        ),
    ]
