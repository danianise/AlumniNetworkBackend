# Generated by Django 4.0.6 on 2022-07-08 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumni_network_app', '0004_alter_post_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
    ]
