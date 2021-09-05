from django.db import models


class AboutUs(models.Model):
    description = models.TextField(null=False, verbose_name='Текст о нас')

    class Meta:
        verbose_name = 'Информация о нас'
        verbose_name_plural = 'Информация о нас'

    def __str__(self):
        return self.description


class Gallery(models.Model):
    about_us = models.ForeignKey(AboutUs, null=True, on_delete=models.SET_NULL, related_name='images')
    image = models.ImageField(upload_to='gallery_images/', null=True, blank=True, verbose_name='Фотография')

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галерея'


class Statistic(models.Model):
    number = models.PositiveIntegerField(verbose_name='Числовое значение')
    description = models.CharField(max_length=255, verbose_name='Краткое описание')

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Информация о нас в цифрах'
        verbose_name_plural = 'Информация о нас в цифрах'


class Course(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название курса')
    description = models.TextField(verbose_name='Краткое описание')
    text = models.TextField(verbose_name='Полное описание')
    age = models.CharField(max_length=250, verbose_name='Возрастная категория')
    duration = models.CharField(max_length=250, verbose_name='Продолжительность курса')
    schedule = models.CharField(max_length=250, verbose_name='График занятий')
    price = models.PositiveIntegerField(verbose_name='Стоимость курса')
    image = models.ImageField(upload_to='gallery_images/', null=True, blank=True, verbose_name='Изображение')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Mentor(models.Model):
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, verbose_name='Курс',
                               related_name='mentors')
    first_name = models.CharField(verbose_name='Имя', max_length=255)
    last_name = models.CharField(verbose_name='Фамилия', max_length=255)
    description = models.TextField(verbose_name='Краткое описание')
    image = models.ImageField(upload_to='mentors-photos/', verbose_name='Фотография')
    status = models.BooleanField(verbose_name='Статус ментора', default=True)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Ментор'
        verbose_name_plural = 'Менторы'


class CourseStudyPlan(models.Model):
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, verbose_name='Курс',
                               related_name='sections')
    section = models.CharField(verbose_name='Название раздела', max_length=255)
    description = models.TextField(verbose_name='Описание раздела')

    class Meta:
        verbose_name = 'План обучения на курсе'
        verbose_name_plural = 'План обучения на курсе'

    def __str__(self):
        return self.section


class CourseProject(models.Model):
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, verbose_name='Курс',
                               related_name='projects')
    image = models.ImageField(upload_to='projects/', verbose_name='Проект')
    description = models.CharField(verbose_name='Описание проекта', max_length=255)

    class Meta:
        verbose_name = 'Выполненные работы на курсе'
        verbose_name_plural = 'Выполненные работы на курсе'

    def __str__(self):
        return self.description


class Application(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=200)
    phone_number = models.CharField(max_length=200, verbose_name='Номер телефона')
    email = models.EmailField(max_length=255, verbose_name='Почта', blank=True, null=True)
    comment = models.CharField(verbose_name='Комментарий', max_length=250, blank=True, null=True)
    sent_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'


class Feedback(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    image = models.ImageField(upload_to='feedbacks-photos/', verbose_name='Фотография')
    comment = models.TextField(verbose_name='Отзыв')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return self.name


class FAQ(models.Model):
    question = models.CharField(max_length=250, verbose_name='Текст вопроса')
    answer = models.TextField(verbose_name='Текст ответа')

    class Meta:
        verbose_name = 'Часто задаваемые вопросы'
        verbose_name_plural = 'Часто задаваемые вопросы'

    def __str__(self):
        return self.question


class Event(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    date = models.DateTimeField(verbose_name='Дата', null=True, blank=True)
    time = models.TimeField(verbose_name='Время', null=True, blank=True)
    location = models.CharField(max_length=255, verbose_name='Адрес', null=True, blank=True)
    image = models.ImageField(upload_to='events-images/', verbose_name='Изображение')

    class Meta:
        verbose_name = 'Новости и мероприятия'
        verbose_name_plural = 'Новости и мероприятия'

    def __str__(self):
        return self.title