# Generated by Django 4.1.7 on 2023-03-21 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0010_remove_logs_user_remove_table_uniqueid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logstable',
            name='uniqueid',
            field=models.CharField(max_length=20),
        ),
    ]