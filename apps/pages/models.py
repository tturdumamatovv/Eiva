from django.db import models
from rest_framework.exceptions import ValidationError


# Create your models here.

class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.pk and self.__class__.objects.exists():
            raise ValidationError(f"Нельзя создать больше одной записи {self.__class__.__name__}.")
        return super().save(*args, **kwargs)


class WelcomePage(SingletonModel):
    image = models.ImageField(upload_to="welcome", verbose_name="Изображение", blank=True, null=True)
    title = models.CharField(max_length=255, verbose_name="Заголовок", blank=True, null=True)
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    text_button = models.CharField(max_length=255, verbose_name="Текст кнопки", blank=True, null=True)
    link_button = models.CharField(max_length=255, verbose_name="Ссылка кнопки", blank=True, null=True)

    def __str__(self):
        return "Welcome Page"

    class Meta:
        verbose_name = "Welcome Page"
        verbose_name_plural = "Welcome Page"


class Advantages(SingletonModel):
    page = models.ForeignKey(WelcomePage, on_delete=models.CASCADE, verbose_name="Страница", blank=True, null=True,
                             related_name='advantages')
    icon = models.FileField(upload_to="advantages", verbose_name="Иконка", blank=True, null=True)
    text = models.CharField(max_length=255, verbose_name="Текст", blank=True, null=True)

    class Meta:
        verbose_name = "Преимущество"
        verbose_name_plural = "Преимущества"


class MainPage(SingletonModel):
    our_services_title = models.CharField(max_length=255, verbose_name="Наши услуги")
    our_specialists_title = models.CharField(max_length=255, verbose_name="Наши специалисты")
    about_us_title = models.CharField(max_length=255, verbose_name="О нас")
    about_us_description = models.TextField(verbose_name="О нас")
    counter_title = models.CharField(max_length=255, verbose_name="Заголовок счетчика")
    counter_sub_title = models.CharField(max_length=255, verbose_name="Подзаголовок счетчика")
    birth_counter = models.IntegerField(default=0, verbose_name="Количество родившихся")
    birth_counter_sub_title = models.CharField(max_length=255, verbose_name="Подзаголовок Количество родившихся")
    boys_counter = models.IntegerField(default=0, verbose_name="Количество мальчиков")
    girls_counter = models.IntegerField(default=0, verbose_name="Количество девочек")

    class Meta:
        verbose_name = "Главная страница"
        verbose_name_plural = "Главные страница"


class AboutPage(SingletonModel):
    title = models.CharField(max_length=255, verbose_name="О нас")
    text = models.TextField(verbose_name="О нас")
    image = models.ImageField(upload_to="about", verbose_name="Изображение")
    counter_1_title = models.CharField(max_length=255, verbose_name="Заголовок счетчика")
    counter_1_value = models.IntegerField(default=0, verbose_name="Значение счетчика")
    counter_2_title = models.CharField(max_length=255, verbose_name="Заголовок счетчика")
    counter_2_value = models.IntegerField(default=0, verbose_name="Значение счетчика")
    counter_3_title = models.CharField(max_length=255, verbose_name="Заголовок счетчика")
    counter_3_value = models.IntegerField(default=0, verbose_name="Значение счетчика")
    cards_title = models.CharField(max_length=255, verbose_name="Заголовок карточек")
    faq_title = models.CharField(max_length=255, verbose_name="Заголовок вопросов")
    partners_title = models.CharField(max_length=255, verbose_name="Заголовок партнеров")
    gallery_title = models.CharField(max_length=255, verbose_name="Заголовок галереи")

    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = "О нас"


class AboutCard(SingletonModel):
    page = models.ForeignKey(AboutPage, on_delete=models.CASCADE, verbose_name="Страница")
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to="about", verbose_name="Изображение")

    class Meta:
        verbose_name = "Карточка о нас"
        verbose_name_plural = "Карточки о нас"


class AboutFAQ(SingletonModel):
    page = models.ForeignKey(AboutPage, on_delete=models.CASCADE, verbose_name="Страница")
    question = models.CharField(max_length=255, verbose_name="Вопрос")
    answer = models.TextField(verbose_name="Ответ")

    class Meta:
        verbose_name = "Вопрос о нас"
        verbose_name_plural = "Вопросы о нас"


class AboutFAQImage(SingletonModel):
    page = models.ForeignKey(AboutPage, on_delete=models.CASCADE, verbose_name="Страница")
    image = models.ImageField(upload_to="about", verbose_name="Изображение")
    link = models.CharField(max_length=255, verbose_name="Ссылка")

    class Meta:
        verbose_name = "Изображение вопроса о нас"
        verbose_name_plural = "Изображения вопросов о нас"


class AboutPartners(SingletonModel):
    page = models.ForeignKey(AboutPage, on_delete=models.CASCADE, verbose_name="Страница")
    image = models.ImageField(upload_to="about/partners", verbose_name="Изображение")

    class Meta:
        verbose_name = "Партнер"
        verbose_name_plural = "Партнеры"


class AboutGallery(SingletonModel):
    page = models.ForeignKey(AboutPage, on_delete=models.CASCADE, verbose_name="Страница")
    name = models.CharField(max_length=255, verbose_name="Имя")
    image = models.ImageField(upload_to="about/gallery", verbose_name="Изображение")

    class Meta:
        verbose_name = "Изображение галереи"
        verbose_name_plural = "Изображения галереи"


class ServicesPage(SingletonModel):
    pass


class DoctorsPage(SingletonModel):
    pass


class PricesPage(SingletonModel):
    pass


class ContactsPage(SingletonModel):
    pass
