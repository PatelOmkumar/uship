# Generated by Django 2.1 on 2021-04-02 20:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dbmodels', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='companyFeedback_TB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Mesg', models.TextField(verbose_name='Message:')),
                ('Feedback_date', models.DateTimeField(auto_now_add=True, verbose_name='Feedback Date:')),
                ('Userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbmodels.User_TB')),
            ],
            options={
                'verbose_name': 'Company FeedBack',
            },
        ),
    ]
