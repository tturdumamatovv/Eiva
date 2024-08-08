# Generated by Django 5.0.7 on 2024-08-07 09:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='О нас')),
                ('text', models.TextField(verbose_name='О нас')),
                ('image', models.ImageField(upload_to='about', verbose_name='Изображение')),
                ('counter_1_title', models.CharField(max_length=255, verbose_name='Заголовок счетчика')),
                ('counter_1_value', models.IntegerField(default=0, verbose_name='Значение счетчика')),
                ('counter_2_title', models.CharField(max_length=255, verbose_name='Заголовок счетчика')),
                ('counter_2_value', models.IntegerField(default=0, verbose_name='Значение счетчика')),
                ('counter_3_title', models.CharField(max_length=255, verbose_name='Заголовок счетчика')),
                ('counter_3_value', models.IntegerField(default=0, verbose_name='Значение счетчика')),
                ('cards_title', models.CharField(max_length=255, verbose_name='Заголовок карточек')),
                ('faq_title', models.CharField(max_length=255, verbose_name='Заголовок вопросов')),
                ('partners_title', models.CharField(max_length=255, verbose_name='Заголовок партнеров')),
                ('gallery_title', models.CharField(max_length=255, verbose_name='Заголовок галереи')),
            ],
            options={
                'verbose_name': 'О нас',
                'verbose_name_plural': 'О нас',
            },
        ),
        migrations.CreateModel(
            name='ContactsPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DoctorsPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MainPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('our_services_title', models.CharField(max_length=255, verbose_name='Наши услуги')),
                ('our_specialists_title', models.CharField(max_length=255, verbose_name='Наши специалисты')),
                ('counter_title', models.CharField(max_length=255, verbose_name='Заголовок счетчика')),
                ('counter_sub_title', models.CharField(max_length=255, verbose_name='Подзаголовок счетчика')),
                ('birth_counter', models.IntegerField(default=0, verbose_name='Количество родившихся')),
                ('boys_counter', models.IntegerField(default=0, verbose_name='Количество мальчиков')),
                ('girls_counter', models.IntegerField(default=0, verbose_name='Количество девочек')),
            ],
            options={
                'verbose_name': 'Главная страница',
                'verbose_name_plural': 'Главные страницы',
            },
        ),
        migrations.CreateModel(
            name='PricesPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ServicesPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WelcomePage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='welcome', verbose_name='Изображение')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('text_button', models.CharField(blank=True, max_length=255, null=True, verbose_name='Текст кнопки')),
                ('link_button', models.CharField(blank=True, max_length=255, null=True, verbose_name='Ссылка кнопки')),
            ],
            options={
                'verbose_name': 'Welcome Page',
                'verbose_name_plural': 'Welcome Pages',
            },
        ),
        migrations.CreateModel(
            name='AboutGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('image', models.ImageField(upload_to='about/gallery', verbose_name='Изображение')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.aboutpage', verbose_name='Страница')),
            ],
            options={
                'verbose_name': 'Изображение галереи',
                'verbose_name_plural': 'Изображения галереи',
            },
        ),
        migrations.CreateModel(
            name='AboutFAQImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='about', verbose_name='Изображение')),
                ('link', models.CharField(max_length=255, verbose_name='Ссылка')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.aboutpage', verbose_name='Страница')),
            ],
            options={
                'verbose_name': 'Изображение вопроса о нас',
                'verbose_name_plural': 'Изображения вопросов о нас',
            },
        ),
        migrations.CreateModel(
            name='AboutFAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255, verbose_name='Вопрос')),
                ('answer', models.TextField(verbose_name='Ответ')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.aboutpage', verbose_name='Страница')),
            ],
            options={
                'verbose_name': 'Вопрос о нас',
                'verbose_name_plural': 'Вопросы о нас',
            },
        ),
        migrations.CreateModel(
            name='AboutCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='about', verbose_name='Изображение')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.aboutpage', verbose_name='Страница')),
            ],
            options={
                'verbose_name': 'Карточка о нас',
                'verbose_name_plural': 'Карточки о нас',
            },
        ),
        migrations.CreateModel(
            name='AboutPartners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='about/partners', verbose_name='Изображение')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.aboutpage', verbose_name='Страница')),
            ],
            options={
                'verbose_name': 'Партнер',
                'verbose_name_plural': 'Партнеры',
            },
        ),
        migrations.CreateModel(
            name='Advantages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(blank=True, max_length=255, null=True, verbose_name='Иконка')),
                ('text', models.CharField(blank=True, max_length=255, null=True, verbose_name='Текст')),
                ('page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='advantages', to='pages.welcomepage', verbose_name='Страница')),
            ],
            options={
                'verbose_name': 'Преимущество',
                'verbose_name_plural': 'Преимущества',
            },
        ),
    ]
