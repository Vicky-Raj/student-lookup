# Generated by Django 2.1.2 on 2019-04-03 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='tutor',
        ),
        migrations.RemoveField(
            model_name='student',
            name='warden',
        ),
    ]