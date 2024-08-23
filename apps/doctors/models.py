from django.db import models


class Position(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название должности')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'


class Specialization(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название специализации')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Спецификация'
        verbose_name_plural = 'Спецификации'


class Doctor(models.Model):
    name = models.CharField(max_length=255, verbose_name='ФИО')
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True, related_name='doctors',
                                 verbose_name='Должность')
    specialization = models.ForeignKey(Specialization, on_delete=models.SET_NULL, null=True, related_name='doctors',
                                       verbose_name='Спецификация')
    image = models.FileField(upload_to='doctors', verbose_name='Фото', blank=True, null=True)
    seniority = models.CharField(max_length=255, verbose_name='Стаж')
    description = models.TextField(null=True, verbose_name='Описание')

    class Meta:
        verbose_name = 'Врач'
        verbose_name_plural = 'Врачи'


class Сertificate(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='certificates', verbose_name='Врач')
    name = models.CharField(max_length=255, verbose_name='Название сертификата')
    image = models.FileField(upload_to='certificates', verbose_name='Файл сертификата')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сертификат'
        verbose_name_plural = 'Сертификаты'


class Review(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='reviews', verbose_name='Врач')
    image = models.FileField(upload_to='reviews', verbose_name='Фото', blank=True, null=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class Photo(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='photos', verbose_name='Врач')
    image = models.FileField(upload_to='photos', verbose_name='Файл фото')

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'


class Order(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя', blank=True, null=True)
    phone = models.CharField(max_length=255, verbose_name='Телефон', blank=True, null=True)
    email = models.EmailField(verbose_name='Email', blank=True, null=True)
    text = models.TextField(verbose_name='Сообщение', blank=True, null=True)
    docktor = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name='Врач', blank=True, null=True)
    packege = models.CharField(max_length=255, verbose_name='Пакет', blank=True, null=True)

    def __str__(self):
        return f'{self.name} {self.phone}'

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
