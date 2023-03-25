# Generated by Django 4.1.7 on 2023-03-23 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0041_alter_logstable_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='id',
            field=models.BigAutoField(auto_created=True, default=None, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='uniqueid',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]