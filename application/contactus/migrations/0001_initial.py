# Generated by Django 2.1 on 2021-04-02 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs_TB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=30, verbose_name='First Name:')),
                ('Last_name', models.CharField(max_length=30, verbose_name='Last Name:')),
                ('Email', models.EmailField(max_length=254, verbose_name='Email ID:')),
                ('Subject', models.CharField(max_length=150, verbose_name='Subject:')),
                ('Mesg', models.TextField(verbose_name='Message:')),
                ('Date', models.DateTimeField(auto_now_add=True, verbose_name='Contact Date:')),
            ],
            options={
                'verbose_name': 'Contact U',
            },
        ),
    ]