# Generated by Django 4.0.6 on 2022-12-15 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni_network_app', '0013_alter_event_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='dateTime',
            field=models.DateTimeField(),
        ),
    ]