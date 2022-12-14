# Generated by Django 2.1 on 2021-04-02 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mes', models.TextField(blank=True, default='', verbose_name='Message')),
                ('phone_number', models.CharField(max_length=150, verbose_name='Phone Number')),
                ('altphone_number', models.CharField(blank=True, max_length=150, verbose_name='Phone Number')),
                ('from_place', models.CharField(blank=True, max_length=150, verbose_name='From')),
                ('To_place', models.CharField(blank=True, max_length=150, verbose_name='To')),
                ('moving_date', models.DateTimeField(verbose_name='Moving Date')),
            ],
        ),
    ]
