# Generated by Django 3.2.8 on 2021-11-27 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('class_app', '0002_auto_20211127_0649'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='semester',
        ),
        migrations.RemoveField(
            model_name='note',
            name='Course',
        ),
        migrations.RemoveField(
            model_name='project',
            name='Course',
        ),
        migrations.DeleteModel(
            name='assignment',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='note',
        ),
        migrations.DeleteModel(
            name='project',
        ),
        migrations.DeleteModel(
            name='semester',
        ),
    ]
