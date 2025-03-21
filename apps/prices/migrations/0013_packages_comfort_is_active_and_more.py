# Generated by Django 5.0.7 on 2024-09-03 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prices', '0012_packages_all_prices'),
    ]

    operations = [
        migrations.AddField(
            model_name='packages',
            name='comfort_is_active',
            field=models.BooleanField(default=True, verbose_name='Комфорт активен'),
        ),
        migrations.AddField(
            model_name='packages',
            name='standard_is_active',
            field=models.BooleanField(default=True, verbose_name='Стандарт активен'),
        ),
        migrations.AddField(
            model_name='packages',
            name='vip_is_active',
            field=models.BooleanField(default=True, verbose_name='VIP активен'),
        ),
    ]
