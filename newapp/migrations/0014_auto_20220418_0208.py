# Generated by Django 3.2.12 on 2022-04-17 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0013_info_dars_dars'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='info_dars',
            name='info',
        ),
        migrations.AddField(
            model_name='info_dars',
            name='info',
            field=models.ManyToManyField(to='newapp.newapp'),
        ),
    ]
