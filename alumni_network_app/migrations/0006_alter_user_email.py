# Generated by Django 4.0.6 on 2022-07-16 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni_network_app', '0005_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
