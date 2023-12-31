# Generated by Django 4.2.2 on 2023-06-20 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hr_system', '0017_alter_employee_department'),
        ('user_profile', '0003_alter_profile_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='employee',
            field=models.OneToOneField(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee_profile', to='hr_system.employee', verbose_name='employee profile'),
        ),
    ]
