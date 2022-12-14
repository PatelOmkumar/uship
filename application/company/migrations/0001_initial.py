# Generated by Django 2.1 on 2021-04-02 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
        ('locality', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company_TB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100, verbose_name='Company Name:')),
                ('company_phone', models.CharField(max_length=11, verbose_name='Company Phone:')),
                ('company_password', models.CharField(max_length=20, verbose_name='Password:')),
                ('company_cpassword', models.CharField(max_length=20, verbose_name='Confirm Password:')),
                ('company_address', models.TextField(verbose_name='Company Address:')),
                ('company_emailid', models.EmailField(max_length=254, unique=True, verbose_name='Company Email ID:')),
                ('company_logo', models.ImageField(upload_to='companylogoimages/', verbose_name='Company Logo:')),
                ('company_desc', models.TextField(verbose_name='Company Description:')),
                ('company_work', models.CharField(choices=[('P', 'Packing'), ('M', 'Moving'), ('PM', 'Both Packing and Moving'), ('SC', 'Scrap Collectors'), ('PMSC', 'Both Packing and Moving with Scrap Collectors')], max_length=4, verbose_name='Company Work:')),
                ('isActive', models.BooleanField(default=False)),
                ('branch', models.ManyToManyField(to='locality.area')),
                ('city', models.ManyToManyField(to='locality.city')),
                ('company_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='category.Category')),
                ('state', models.ManyToManyField(to='locality.state')),
            ],
            options={
                'verbose_name': 'Company Register',
            },
        ),
    ]
