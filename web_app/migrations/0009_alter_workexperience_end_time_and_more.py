# Generated by Django 5.0.2 on 2024-03-06 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0008_rename_skillsection_skills_rename_skill_techskill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workexperience',
            name='end_time',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='start_time',
            field=models.CharField(max_length=20),
        ),
    ]
