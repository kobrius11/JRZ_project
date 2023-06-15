# Generated by Django 4.2.2 on 2023-06-15 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr_system', '0004_remove_application_content_application_template'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='content',
            field=models.TextField(blank=True, null=True, verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='application',
            name='template',
            field=models.CharField(choices=[(0, 'Vacation form'), (1, 'Termination form')], db_index=True, max_length=50, verbose_name='template'),
        ),
    ]
