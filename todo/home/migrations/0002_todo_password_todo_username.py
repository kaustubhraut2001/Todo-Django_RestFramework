# Generated by Django 5.0.6 on 2024-07-05 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='password',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AddField(
            model_name='todo',
            name='username',
            field=models.CharField(default='', max_length=120),
        ),
    ]
