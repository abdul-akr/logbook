# Generated by Django 4.1.7 on 2023-03-24 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LogTable', '0013_roles_remove_user_role_user_roles'),
    ]

    operations = [
        migrations.AddField(
            model_name='roles',
            name='uniqueid',
            field=models.CharField(default=None, max_length=20),
            preserve_default=False,
        ),
    ]