# Generated by Django 4.0.6 on 2022-07-07 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni_network_app', '0003_rename_network_user_networks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(default='anonymous', max_length=100),
        ),
    ]