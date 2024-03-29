# Generated by Django 4.1.7 on 2023-03-27 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LogTable', '0021_roles_id_user_id_alter_roles_role_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.ManyToManyField(to='LogTable.role'),
        ),
    ]
