# Generated by Django 5.0.7 on 2024-11-04 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0006_doctor_order_alter_order_docktor'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='doctor',
            options={'ordering': ['order'], 'verbose_name': 'Врач', 'verbose_name_plural': 'Врачи'},
        ),
    ]
