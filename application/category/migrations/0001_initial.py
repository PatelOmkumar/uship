# Generated by Django 2.1 on 2021-04-02 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
                ('cate_des', models.TextField(default='')),
                ('cate_img', models.ImageField(default='', upload_to='cateimages/')),
                ('status', models.BooleanField(default=False)),
                ('Dateandtime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
