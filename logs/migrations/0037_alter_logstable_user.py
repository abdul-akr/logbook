# Generated by Django 4.1.7 on 2023-03-23 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0036_remove_user_id_alter_user_uniqueid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logstable',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='logs', to='logs.user'),
        ),
    ]