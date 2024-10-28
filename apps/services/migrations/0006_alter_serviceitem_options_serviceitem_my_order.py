# Generated by Django 5.0.7 on 2024-10-28 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_alter_serviceitem_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='serviceitem',
            options={'ordering': ['my_order'], 'verbose_name': 'Элемент сервиса', 'verbose_name_plural': 'Элементы сервиса'},
        ),
        migrations.AddField(
            model_name='serviceitem',
            name='my_order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
