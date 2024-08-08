from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название услуги')
    description = models.TextField(verbose_name='Описание')
    price = models.IntegerField(verbose_name='Цена')
    verbose_name = 'Услуга'
    verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class Package(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название пакета')
    description = models.TextField(verbose_name='Описание')
    price = models.IntegerField(verbose_name='Цена')
    services = models.ManyToManyField(Service, verbose_name='Услуги')
    verbose_name = 'Пакет'
    verbose_name_plural = 'Пакеты'

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пакет'
        verbose_name_plural = 'Пакеты'