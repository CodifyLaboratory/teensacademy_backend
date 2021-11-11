from django.db import models


class AboutUs(models.Model):
    description = models.TextField(verbose_name='Текст', null=True, blank=True)

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'

    def __str__(self):
        return self.description


class Gallery(models.Model):
    about_us = models.ForeignKey(AboutUs, null=True, on_delete=models.SET_NULL, related_name='images')
    image = models.ImageField(upload_to='gallery_images/', null=True, blank=True, verbose_name='Фотография')

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галерея'


class Statistic(models.Model):
    number = models.CharField(verbose_name='Числовое значение', max_length=255)
    description = models.CharField(max_length=255, verbose_name='Краткое описание', null=True, blank=True)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'О нас в цифрах'
        verbose_name_plural = 'О нас в цифрах'


class Course(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название курса', null=True, blank=True)
    description = models.TextField(verbose_name='Краткое описание', null=True, blank=True)
    text = models.TextField(verbose_name='Полное описание', null=True, blank=True)
    age = models.CharField(max_length=250, verbose_name='Возрастная категория')
    duration = models.CharField(max_length=250, verbose_name='Продолжительность курса', null=True, blank=True)
    schedule = models.CharField(max_length=250, verbose_name='График занятий', null=True, blank=True)
    price = models.CharField(max_length=250, verbose_name='Стоимость курса', null=True, blank=True)
    image = models.ImageField(upload_to='gallery_images/', null=True, blank=True, verbose_name='Изображение')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Mentor(models.Model):
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, verbose_name='Курс',
                               related_name='mentors')
    first_name = models.CharField(verbose_name='Имя', max_length=255, null=True, blank=True)
    last_name = models.CharField(verbose_name='Фамилия', max_length=255, null=True, blank=True)
    description = models.TextField(verbose_name='Краткое описание', null=True, blank=True)
    image = models.ImageField(upload_to='mentors-photos/', verbose_name='Фотография')

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Ментор'
        verbose_name_plural = 'Менторы'


class CourseStudyPlan(models.Model):
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, verbose_name='Курс',
                               related_name='sections')
    section = models.CharField(verbose_name='Название раздела', max_length=255, null=True, blank=True)
    description = models.TextField(verbose_name='Описание раздела', null=True, blank=True)

    class Meta:
        verbose_name = 'План обучения'
        verbose_name_plural = 'План обучения'

    def __str__(self):
        return self.section


class CourseProject(models.Model):
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, verbose_name='Курс',
                               related_name='projects')
    image = models.ImageField(upload_to='projects/', verbose_name='Проект')
    description = models.CharField(verbose_name='Описание проекта', null=True, blank=True, max_length=255)

    class Meta:
        verbose_name = 'Пример работ'
        verbose_name_plural = 'Примеры работ'

    def __str__(self):
        return self.description


class Feedback(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя', null=True, blank=True)
    image = models.ImageField(upload_to='feedbacks-photos/', verbose_name='Фотография', null=True, blank=True)
    comment = models.TextField(verbose_name='Отзыв', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return self.name


class FAQ(models.Model):
    question = models.CharField(max_length=250, verbose_name='Текст вопроса', null=True, blank=True)
    answer = models.TextField(verbose_name='Текст ответа', null=True, blank=True)

    class Meta:
        verbose_name = 'Часто задаваемые вопросы'
        verbose_name_plural = 'Часто задаваемые вопросы'

    def __str__(self):
        return self.question


class Event(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название', null=True, blank=True)
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    date = models.DateField(verbose_name='Дата', null=True, blank=True)
    time = models.TimeField(verbose_name='Время', null=True, blank=True)
    location = models.CharField(max_length=255, verbose_name='Адрес', null=True, blank=True)
    image = models.ImageField(upload_to='events-images/', verbose_name='Изображение')

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'

    def __str__(self):
        return self.title


class Certificate(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название', null=True, blank=True)
    image = models.ImageField(upload_to='certificate-photos/', verbose_name='Сертификаты')

    class Meta:
        verbose_name = 'Сертификат'
        verbose_name_plural = 'Сертификаты'

    def __str__(self):
        return self.name
