from django.db import models
from rest_framework.exceptions import ValidationError


# Create your models here.


class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.pk and self.__class__.objects.exists():
            raise ValidationError(
                f"Нельзя создать больше одной записи {self.__class__.__name__}."
            )
        return super().save(*args, **kwargs)


class WelcomePage(SingletonModel):
    image = models.FileField(
        upload_to="welcome", verbose_name="Изображение", blank=True, null=True
    )
    title = models.CharField(
        max_length=255, verbose_name="Заголовок", blank=True, null=True
    )
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    text_button = models.CharField(
        max_length=255, verbose_name="Текст кнопки", blank=True, null=True
    )
    link_button = models.CharField(
        max_length=255, verbose_name="Ссылка кнопки", blank=True, null=True
    )

    def __str__(self):
        return "Welcome Page"

    class Meta:
        verbose_name = "Welcome Page"
        verbose_name_plural = "Welcome Page"


class Advantages(models.Model):
    page = models.ForeignKey(
        WelcomePage,
        on_delete=models.CASCADE,
        verbose_name="Страница",
        blank=True,
        null=True,
        related_name="advantages",
    )
    icon = models.FileField(
        upload_to="advantages", verbose_name="Иконка", blank=True, null=True
    )
    text = models.CharField(max_length=255, verbose_name="Текст", blank=True, null=True)

    def __str__(self):
        return self.text[0:15]

    class Meta:
        verbose_name = "Преимущество"
        verbose_name_plural = "Преимущества"


class MainPage(SingletonModel):
    our_services_title = models.CharField(max_length=255, verbose_name="Наши услуги")
    our_specialists_title = models.CharField(
        max_length=255, verbose_name="Наши специалисты"
    )
    about_us_title = models.CharField(max_length=255, verbose_name="О нас")
    about_us_description = models.TextField(verbose_name="О нас")
    about_us_image = models.FileField(
        upload_to="about", verbose_name="Изображение", blank=True, null=True
    )
    counter_title = models.CharField(max_length=255, verbose_name="Заголовок счетчика")
    counter_sub_title = models.CharField(
        max_length=255, verbose_name="Подзаголовок счетчика"
    )
    birth_counter = models.IntegerField(default=0, verbose_name="Количество родившихся")
    birth_counter_sub_title = models.CharField(
        max_length=255, verbose_name="Подзаголовок Количество родившихся"
    )
    boys_counter = models.IntegerField(default=0, verbose_name="Количество мальчиков")
    girls_counter = models.IntegerField(default=0, verbose_name="Количество девочек")

    class Meta:
        verbose_name = "Главная страница"
        verbose_name_plural = "Главные страница"


class AboutPage(SingletonModel):
    title = models.CharField(max_length=255, verbose_name="О нас")
    text = models.TextField(verbose_name="О нас")
    image = models.FileField(
        upload_to="about", verbose_name="Изображение", blank=True, null=True
    )
    counter_1_title = models.CharField(
        max_length=255, verbose_name="Заголовок счетчика"
    )
    counter_1_value = models.IntegerField(default=0, verbose_name="Значение счетчика")
    counter_2_title = models.CharField(
        max_length=255, verbose_name="Заголовок счетчика"
    )
    counter_2_value = models.IntegerField(default=0, verbose_name="Значение счетчика")
    counter_3_title = models.CharField(
        max_length=255, verbose_name="Заголовок счетчика"
    )
    counter_3_value = models.IntegerField(default=0, verbose_name="Значение счетчика")
    cards_title = models.CharField(max_length=255, verbose_name="Заголовок карточек")
    faq_title = models.CharField(max_length=255, verbose_name="Заголовок вопросов")
    partners_title = models.CharField(
        max_length=255, verbose_name="Заголовок партнеров"
    )
    gallery_title = models.CharField(max_length=255, verbose_name="Заголовок галереи")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = "О нас"


class AboutCard(models.Model):
    page = models.ForeignKey(
        AboutPage,
        on_delete=models.CASCADE,
        verbose_name="Страница",
        related_name="cards",
    )
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    image = models.FileField(
        upload_to="about", verbose_name="Изображение", blank=True, null=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Карточка о нас"
        verbose_name_plural = "Карточки о нас"


class AboutFAQ(models.Model):
    page = models.ForeignKey(
        AboutPage,
        on_delete=models.CASCADE,
        verbose_name="Страница",
        related_name="faqs",
    )
    question = models.CharField(max_length=255, verbose_name="Вопрос")
    answer = models.TextField(verbose_name="Ответ")

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = "Вопрос о нас"
        verbose_name_plural = "Вопросы о нас"


class AboutFAQImage(models.Model):
    page = models.ForeignKey(
        AboutPage,
        on_delete=models.CASCADE,
        verbose_name="Страница",
        related_name="faq_images",
    )
    image = models.FileField(
        upload_to="about", verbose_name="Изображение", blank=True, null=True
    )
    link = models.CharField(max_length=255, verbose_name="Ссылка")

    class Meta:
        verbose_name = "Изображение вопроса о нас"
        verbose_name_plural = "Изображения вопросов о нас"


class AboutPartners(models.Model):
    page = models.ForeignKey(
        AboutPage,
        on_delete=models.CASCADE,
        verbose_name="Страница",
        related_name="partners",
    )
    image = models.FileField(
        upload_to="about/partners", verbose_name="Изображение", blank=True, null=True
    )

    def __str__(self):
        return "Партнер {}".format(self.id)

    class Meta:
        verbose_name = "Партнер"
        verbose_name_plural = "Партнеры"


class AboutImages(models.Model):
    partner = models.ForeignKey(
        AboutPartners,
        on_delete=models.CASCADE,
        verbose_name="Партнер",
        blank=True,
        null=True,
    )
    image = models.FileField(
        upload_to="about-images", verbose_name="Изображение", blank=True, null=True
    )

    def __str__(self):
        return "Изображение {}".format(self.id)

    class Meta:
        verbose_name = "Изображение партнера"
        verbose_name_plural = "Изображения партнеров"


class AboutGallery(models.Model):
    page = models.ForeignKey(
        AboutPage,
        on_delete=models.CASCADE,
        verbose_name="Страница",
        related_name="gallery",
    )
    name = models.CharField(max_length=255, verbose_name="Имя")
    image = models.FileField(
        upload_to="about/gallery", verbose_name="Изображение", blank=True, null=True
    )
    plaseholder = models.FileField(
        upload_to="about/gallery", verbose_name="Плейсхолдер", blank=True, null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Изображение галереи"
        verbose_name_plural = "Изображения галереи"


class ContactInformation(SingletonModel):
    address = models.TextField(verbose_name="Адрес")
    working_hours_weekdays = models.CharField(max_length=50, verbose_name="Часы работы")
    working_hours_sticionar = models.CharField(
        max_length=50, verbose_name="Часы работы стационара", blank=True, null=True
    )
    working_hours_polyclinic = models.CharField(
        max_length=50, verbose_name="Часы работы поликлиники", blank=True, null=True
    )
    email = models.EmailField(verbose_name="Электронная почта")
    iframe_map = models.TextField(
        verbose_name="Код карты", help_text="HTML iframe для встраивания карты"
    )

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = "Контактная информация"
        verbose_name_plural = "Контактная информация"


class PhoneNumber(models.Model):
    number = models.CharField(max_length=20, verbose_name="Номер телефона")
    contact_information = models.ForeignKey(
        "ContactInformation",
        on_delete=models.CASCADE,
        related_name="phone_numbers",
        verbose_name="Контактная информация",
    )

    def __str__(self):
        return f"{self.number}"

    class Meta:
        verbose_name = "Телефонный номер"
        verbose_name_plural = "Телефонные номера"


class SocialNetwork(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название социальной сети")
    url = models.URLField(verbose_name="URL")
    icon = models.FileField(
        upload_to="social_networks", verbose_name="Иконка", blank=True, null=True
    )
    contact_information = models.ForeignKey(
        "ContactInformation",
        on_delete=models.CASCADE,
        related_name="social_networks",
        verbose_name="Контактная информация",
    )

    def __str__(self):
        return f"{self.name}: {self.url}"

    class Meta:
        verbose_name = "Социальная сеть"
        verbose_name_plural = "Социальные сети"


class Email(models.Model):
    email = models.EmailField(verbose_name="Электронная почта")
    contact_information = models.ForeignKey(
        "ContactInformation",
        on_delete=models.CASCADE,
        related_name="emails",
        verbose_name="Контактная информация",
    )

    def __str__(self):
        return f"{self.email}"

    class Meta:
        verbose_name = "Электронная почта"
        verbose_name_plural = "Электронные почты"


class Documents(SingletonModel):
    pass

    def __str__(self):
        return "Документы"

    class Meta:
        verbose_name = "Документы"
        verbose_name_plural = "Документы"


class Document(models.Model):
    document = models.ForeignKey(
        Documents,
        on_delete=models.CASCADE,
        verbose_name="Документ",
        related_name="documents",
    )
    name = models.CharField(max_length=255, verbose_name="Тип документа")
    text = models.TextField(verbose_name="Текст", blank=True, null=True)
    file = models.FileField(
        upload_to="documents", verbose_name="Файл", blank=True, null=True
    )

    class Meta:
        verbose_name = "Документ"
        verbose_name_plural = "Документ"

    def __str__(self):
        return self.name


class MetaData(SingletonModel):
    meta_title = models.CharField(
        max_length=255, verbose_name="Мета заголовок", blank=True, null=True
    )
    meta_description = models.CharField(
        max_length=255, verbose_name="Мета описание", blank=True, null=True
    )
    meta_image = models.FileField(
        upload_to="meta_images", verbose_name="Мета изображение", blank=True, null=True
    )
    keywords = models.TextField(
        max_length=255, verbose_name="Ключевые слова", blank=True, null=True
    )

    def __str__(self):
        return "Метаданные"

    class Meta:
        verbose_name = "Метаданные"
        verbose_name_plural = "Метаданные"


class FormBackgroundImage(SingletonModel):
    main_background = models.FileField(
        blank=True, null=True, verbose_name='Изображение заднего фона для "Главной страницы"'
    )
    about_background = models.FileField(
        blank=True, null=True, verbose_name='Изображение заднего фона для "О нас"'

    )
    directions_background = models.FileField(
        blank=True, null=True, verbose_name='Изображение заднего фона для "Направления"'
    )
    doctors_background = models.FileField(
        blank=True, null=True, verbose_name='Изображение заднего фона для "Врачи"'

    )
    prices_background = models.FileField(
        blank=True, null=True, verbose_name='Изображение заднего фона для "Цены"'
    )
    docs_background = models.FileField(
        blank=True, null=True, verbose_name='Изображение заднего фона для "Документы"'

    )
    contacts_background = models.FileField(
        blank=True, null=True, verbose_name='Изображение заднего фона для "Контакты"'

    )


    def __str__(self):
        return "Изображение заднего фона"

    class Meta:
        verbose_name = "Изображение заднего фона"
        verbose_name_plural = "Изображения заднего фона"
