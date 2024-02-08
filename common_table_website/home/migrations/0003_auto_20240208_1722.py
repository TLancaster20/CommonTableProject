# Generated by Django 3.2.24 on 2024-02-08 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20240208_1715'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffprofile',
            name='profilepic',
            field=models.ImageField(default='static/images/profdefault.png', upload_to=''),
        ),
        migrations.AlterField(
            model_name='staffprofile',
            name='bio',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AlterField(
            model_name='staffprofile',
            name='email',
            field=models.EmailField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='staffprofile',
            name='firstname',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='staffprofile',
            name='lastname',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='staffprofile',
            name='pronouns',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='staffprofile',
            name='role',
            field=models.CharField(default='', max_length=30),
        ),
    ]
