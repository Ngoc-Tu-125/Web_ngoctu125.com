# Generated by Django 5.0.2 on 2024-03-08 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0009_alter_workexperience_end_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='techsharing',
            name='is_hidden',
            field=models.BooleanField(default=False),
        ),
    ]
