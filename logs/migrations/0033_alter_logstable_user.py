# Generated by Django 4.1.7 on 2023-03-23 19:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0032_alter_logstable_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logstable',
            name='user',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='logs', to='logs.user'),
        ),
    ]
