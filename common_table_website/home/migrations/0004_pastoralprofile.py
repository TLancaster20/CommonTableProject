# Generated by Django 3.2.24 on 2024-02-10 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20240208_1722'),
    ]

    operations = [
        migrations.CreateModel(
            name='PastoralProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(default='', max_length=255)),
                ('lastname', models.CharField(default='', max_length=255)),
                ('pronouns', models.CharField(default='', max_length=30)),
                ('profilepic', models.ImageField(default='static/images/profdefault.png', upload_to='')),
                ('role', models.CharField(default='', max_length=30)),
                ('email', models.EmailField(default='', max_length=100)),
                ('bio', models.CharField(default='', max_length=2000)),
            ],
        ),
    ]
