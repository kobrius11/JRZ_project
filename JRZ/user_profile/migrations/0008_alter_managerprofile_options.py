# Generated by Django 4.2.2 on 2023-06-22 07:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0007_alter_managerprofile_manager'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='managerprofile',
            options={'verbose_name': 'manager profile', 'verbose_name_plural': 'manager profiles'},
        ),
    ]
