# Generated by Django 4.2.2 on 2023-06-15 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hr_system', '0006_application_status_employee_hire_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='hr_system.department', verbose_name='department'),
        ),
    ]
