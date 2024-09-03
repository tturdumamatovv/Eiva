from django.db import models

from apps.pages.models import SingletonModel


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название категории")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория цен"
        verbose_name_plural = "Категории цен"


class Service(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="Категория",
        blank=True,
        null=True,
    )
    name = models.CharField(max_length=255, verbose_name="Название услуги")
    price = models.CharField(max_length=255, verbose_name="Цена", blank=True, null=True)
    tooltip = models.TextField(
        max_length=255, verbose_name="Подсказка", blank=True, null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Цена"
        verbose_name_plural = "Цены"


class Packages(SingletonModel):
    name_standard = models.CharField(
        max_length=255, verbose_name="Название стандарт пакета"
    )
    price_standard = models.CharField(
        max_length=255, verbose_name="Цена стандарт", blank=True, null=True
    )
    document_package_standard = models.FileField(
        verbose_name="Документ пакета", blank=True, null=True
    )
    document_medicine_standard = models.FileField(
        verbose_name="Документ медикаментов", blank=True, null=True
    )
    standard_is_active = models.BooleanField(
        verbose_name="Стандарт активен", default=True
    )

    name_comfort = models.CharField(
        max_length=255, verbose_name="Название комфорт пакета", blank=True, null=True
    )
    price_comfort = models.CharField(
        max_length=255, verbose_name="Цена комфорт", blank=True, null=True
    )
    document_package_comfort = models.FileField(
        verbose_name="Документ пакета", blank=True, null=True
    )
    document_medicine_comfort = models.FileField(
        verbose_name="Документ медикаментов", blank=True, null=True
    )
    comfort_is_active = models.BooleanField(
        verbose_name="Комфорт активен", default=True
    )

    name_vip = models.CharField(
        max_length=255, verbose_name="Название VIP пакета", blank=True, null=True
    )
    price_vip = models.CharField(
        max_length=255, verbose_name="Цена VIP", blank=True, null=True
    )
    document_package_vip = models.FileField(
        verbose_name="Документ пакета", blank=True, null=True
    )
    document_medicine_vip = models.FileField(
        verbose_name="Документ медикаментов", blank=True, null=True
    )
    vip_is_active = models.BooleanField(verbose_name="VIP активен", default=True)

    all_prices = models.FileField(
        verbose_name="Все цены", blank=True, null=True, upload_to="prices"
    )

    def __str__(self):
        return "Пакеты"

    class Meta:
        verbose_name = "Пакет"
        verbose_name_plural = "Пакеты"


class PackageServiceType(models.Model):
    package = models.ForeignKey(
        Packages,
        on_delete=models.CASCADE,
        verbose_name="Пакет",
        blank=True,
        null=True,
        related_name="types",
    )
    name = models.CharField(
        max_length=255, verbose_name="Название", blank=True, null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип сервиса в пакете"
        verbose_name_plural = "Типы сервисов в пакете"


class PackageService(models.Model):
    type = models.ForeignKey(
        PackageServiceType,
        on_delete=models.CASCADE,
        verbose_name="Тип",
        blank=True,
        null=True,
        related_name="services",
    )
    name = models.CharField(
        max_length=255, verbose_name="Название", blank=True, null=True
    )
    price = models.CharField(max_length=255, verbose_name="Цена", blank=True, null=True)
    price_comfort = models.CharField(
        max_length=255, verbose_name="Цена комфорт", blank=True, null=True
    )
    available_in_comfort = models.BooleanField(
        verbose_name="Доступна в комфорте", default=False, null=True
    )
    price_vip = models.CharField(
        max_length=255, verbose_name="Цена vip", blank=True, null=True
    )
    available_in_vip = models.BooleanField(
        verbose_name="Доступна в vip", default=True, null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Услуга пакета"
        verbose_name_plural = "Услуги пакета"
