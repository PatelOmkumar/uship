# Generated by Django 2.1 on 2021-04-03 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbmodels', '0004_auto_20210403_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company_table',
            name='company_desc',
            field=models.TextField(default='', null=True, verbose_name='Company Description:'),
        ),
    ]
