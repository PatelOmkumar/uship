# Generated by Django 2.1 on 2021-04-02 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dbmodels', '0001_initial'),
        ('complaint', '0001_initial'),
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaints_tb',
            name='Userid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbmodels.User_TB'),
        ),
        migrations.AddField(
            model_name='complaints_tb',
            name='company_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Company_TB'),
        ),
    ]
