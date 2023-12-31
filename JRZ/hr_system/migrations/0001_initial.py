# Generated by Django 4.2.2 on 2023-06-15 10:43

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(verbose_name='date_created')),
                ('content', tinymce.models.HTMLField(choices=[(0, 'Vacation form')])),
            ],
            options={
                'verbose_name': 'application',
                'verbose_name_plural': 'applications',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='name')),
            ],
            options={
                'verbose_name': 'department',
                'verbose_name_plural': 'departments',
            },
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=50, verbose_name='first name')),
                ('l_name', models.CharField(max_length=50, verbose_name='last name')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
            ],
            options={
                'verbose_name': 'manager',
                'verbose_name_plural': 'managers',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=50, verbose_name='first name')),
                ('l_name', models.CharField(max_length=50, verbose_name='last name')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='hr_system.department', verbose_name='employee')),
            ],
            options={
                'verbose_name': 'employee',
                'verbose_name_plural': 'employees',
            },
        ),
        migrations.AddField(
            model_name='department',
            name='manager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departments', to='hr_system.manager', verbose_name='manager'),
        ),
    ]
