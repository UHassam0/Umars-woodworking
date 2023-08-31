# Generated by Django 3.2.20 on 2023-08-31 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getting_projects', '0002_auto_20230831_1940'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ExampleProject',
            new_name='Project',
        ),
        migrations.AlterField(
            model_name='booking',
            name='booking_status',
            field=models.IntegerField(choices=[(0, 'Accepted'), (1, 'Discussed'), (2, 'Rejected'), (3, 'Pending')], default=3),
        ),
    ]
