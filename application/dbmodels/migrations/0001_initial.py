# Generated by Django 2.1 on 2021-04-02 16:16

import dbmodels.validators
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
        ('locality', '0001_initial'),
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_user', models.BooleanField(default=False)),
                ('is_company', models.BooleanField(default=False)),
                ('first_name', models.CharField(max_length=15, verbose_name='First Name:')),
                ('last_name', models.CharField(max_length=15, verbose_name='Last Name:')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Company_table',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('company_name', models.CharField(max_length=100, verbose_name='Company Name:')),
                ('company_phone', models.CharField(max_length=11, verbose_name='Company Phone:')),
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
        migrations.CreateModel(
            name='User_TB',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='M', max_length=1, verbose_name='Gender:')),
                ('phone', models.CharField(max_length=11, verbose_name='Phone No:')),
                ('address', models.TextField(verbose_name='Address:')),
                ('profile_pic', models.ImageField(upload_to='userprofilepicimages', validators=[dbmodels.validators.validate_file_extension])),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='area_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='area', to='locality.area'),
        ),
        migrations.AddField(
            model_name='user',
            name='city_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='city', to='locality.city'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]