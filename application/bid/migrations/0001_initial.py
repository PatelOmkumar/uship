# Generated by Django 2.1 on 2021-04-02 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bidding_date', models.DateTimeField(auto_now_add=True, verbose_name='Bidding Date:')),
                ('price', models.DecimalField(decimal_places=3, max_digits=7, verbose_name='Bidding Price:')),
                ('max_price', models.TextField(blank=True, default='', verbose_name='Base Price')),
            ],
            options={
                'verbose_name': 'Bidding',
            },
        ),
    ]
