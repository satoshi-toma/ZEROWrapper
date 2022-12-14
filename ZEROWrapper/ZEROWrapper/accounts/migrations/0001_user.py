# Generated by Django 3.1.2 on 2022-05-27 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=100)),
                ('employee_number', models.PositiveIntegerField(blank=True, help_text='*TMC従業員は必須', null=True)),
                ('department', models.CharField(help_text='例)高岡工場車体部', max_length=100)),
                ('division', models.CharField(blank=True, help_text='例)技術員室/1ボデー課', max_length=100, null=True)),
                ('group', models.CharField(blank=True, help_text='例)1ボデーGr/KT911組', max_length=100, null=True)),
                ('phone_number', models.PositiveIntegerField(help_text='例)数字のみ。ハイフン(-)なしで記入')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
