# Generated by Django 3.2.8 on 2021-11-28 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('class_app', '0004_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='singn_up',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('student_class', models.CharField(max_length=250)),
                ('phone_number', models.CharField(max_length=250)),
                ('password', models.CharField(max_length=250)),
                ('student_ID', models.CharField(max_length=250)),
            ],
        ),
    ]
