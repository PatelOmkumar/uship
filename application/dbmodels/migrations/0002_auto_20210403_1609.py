# Generated by Django 2.1 on 2021-04-03 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dbmodels', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='area_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='city_name',
        ),
    ]
