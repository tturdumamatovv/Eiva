# Generated by Django 5.0.7 on 2024-09-13 05:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prices', '0014_packages_acheges_for_pregnancy_packages_all_packeges'),
    ]

    operations = [
        migrations.RenameField(
            model_name='packages',
            old_name='all_packeges',
            new_name='all_packages',
        ),
        migrations.RenameField(
            model_name='packages',
            old_name='acheges_for_pregnancy',
            new_name='package_for_pregnancy',
        ),
    ]
