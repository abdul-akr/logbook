# Generated by Django 4.1.7 on 2023-03-21 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0012_logstable_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='logstable',
            name='user',
        ),
    ]
