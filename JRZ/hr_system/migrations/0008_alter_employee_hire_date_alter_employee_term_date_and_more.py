# Generated by Django 4.2.2 on 2023-06-16 05:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hr_system', '0007_alter_employee_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='hire_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='hire date'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='term_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='termination date'),
        ),
        migrations.AlterField(
            model_name='manager',
            name='hire_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='hire date'),
        ),
        migrations.AlterField(
            model_name='manager',
            name='term_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='termination date'),
        ),
    ]
