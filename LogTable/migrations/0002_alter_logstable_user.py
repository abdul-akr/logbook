# Generated by Django 4.1.7 on 2023-03-23 20:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LogTable', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logstable',
            name='user',
            field=models.ForeignKey(blank=True, default=123, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='logs', to='LogTable.user'),
        ),
    ]
