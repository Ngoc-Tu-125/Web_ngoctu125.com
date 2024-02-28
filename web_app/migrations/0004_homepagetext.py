# Generated by Django 5.0.2 on 2024-02-28 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0003_alter_techsharing_topic'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePageText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(choices=[('home_intro', 'Home Introduction'), ('home_about', 'Home About'), ('home_tech_sharing', 'Home Tech Sharing'), ('home_github_repo', 'Home Github Repository')], max_length=100, unique=True)),
                ('content', models.TextField()),
            ],
        ),
    ]
