# Generated by Django 3.2.20 on 2023-09-01 23:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('getting_projects', '0003_auto_20230831_1952'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='slug',
        ),
    ]
