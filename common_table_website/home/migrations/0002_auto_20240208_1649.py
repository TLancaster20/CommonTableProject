# Generated by Django 3.2.24 on 2024-02-08 21:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staffprofile',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='staffprofile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='staffprofile',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='staffprofile',
            name='lastname',
        ),
        migrations.RemoveField(
            model_name='staffprofile',
            name='pronouns',
        ),
        migrations.RemoveField(
            model_name='staffprofile',
            name='role',
        ),
    ]
