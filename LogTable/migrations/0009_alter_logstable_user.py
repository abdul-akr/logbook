# Generated by Django 4.1.7 on 2023-03-24 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LogTable', '0008_alter_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logstable',
            name='user',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='logs', to='LogTable.user'),
        ),
    ]