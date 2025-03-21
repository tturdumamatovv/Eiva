from ckeditor.fields import RichTextField
from django.db import models
from django.utils.text import slugify
from unidecode import unidecode


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название категории')
    title = models.CharField(max_length=100, blank=True, null=True, verbose_name='Заголовок')
    icon = models.FileField(upload_to='categories', blank=True, null=True, verbose_name='Иконка')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    order = models.PositiveIntegerField(default=0, editable=False, db_index=True, verbose_name='Порядок')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode(self.name))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['order']


class Type(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Тип сервиса')
    name = models.CharField(max_length=100, verbose_name='Название типа')
    title = models.CharField(max_length=100, blank=True, null=True, verbose_name='Заголовок')
    subtitle = models.CharField(max_length=100, blank=True, null=True, verbose_name='Подзаголовок')
    order = models.PositiveIntegerField(default=0, editable=False, db_index=True, verbose_name='Порядок')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'
        ordering = ['order']


class Service(models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Название сервиса')
    order = models.PositiveIntegerField(default=0, editable=False, db_index=True, verbose_name='Порядок')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Сервис'
        verbose_name_plural = 'Сервисы'
        ordering = ['order']


class ServiceItem(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    text = RichTextField(blank=True, null=True, verbose_name='Текст')
    image = models.FileField(upload_to='services', blank=True, null=True, verbose_name='Изображение')
    image_duration = models.CharField(choices=[('left', 'Слева'), ('right', 'Справа')], max_length=5, default='left', verbose_name='Расположение изображения')

    my_order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Элемент сервиса'
        verbose_name_plural = 'Элементы сервиса'
        ordering = ["my_order"]
