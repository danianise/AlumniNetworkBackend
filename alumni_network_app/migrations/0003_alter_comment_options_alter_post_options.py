# Generated by Django 4.0.6 on 2022-07-09 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumni_network_app', '0002_alter_post_network'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['timestamp']},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['timestamp']},
        ),
    ]
