# Generated by Django 4.1.7 on 2023-03-24 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LogTable', '0016_alter_roles_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roles',
            name='user',
            field=models.ForeignKey(blank=True, choices=[(1, 'manager'), (2, 'employee'), (3, 'admin'), (4, 'supervisor')], default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='role_names', to='LogTable.user'),
        ),
    ]
