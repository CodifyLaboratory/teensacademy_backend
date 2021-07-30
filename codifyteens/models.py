from django.db import models


# Create your models here.
class AboutUs(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок", null=True)
    description = models.TextField(null=False, verbose_name="")
    image = models.ImageField(upload_to="about_us_image", null=True, blank=True, verbose_name="Изображение")

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'O нас'

    def __str__(self):
        return self.title

class AboutUsImage(models.Model):

    title = models.CharField(verbose_name='Заголовок', max_length=255, blank=True, null=True)
    images = models.ImageField(upload_to='about-us', verbose_name='Изображение')
    about = models.ForeignKey(AboutUs, on_delete=models.CASCADE, related_name='images')

    class Meta:
        verbose_name = 'Изображение (О нас)'
        verbose_name_plural = 'Изображении (О нас)'

    def __str__(self):
        return self.title

class Advantages(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок", null=True)
    image = models.ImageField(upload_to="advantages", null=True, blank=True, verbose_name="Изображение")

    class Meta:
        verbose_name = 'Наши преимущества'
        verbose_name_plural = 'Наши преимущества'

    def __str__(self):
        return self.title


class Contact(models.Model):
    address = models.CharField(max_length=255, verbose_name="Адрес")
    mail = models.CharField(max_length=255, verbose_name="Почта")
    phone_number = models.CharField(max_length=20, verbose_name="Номер Телефона")
    phone_number2 = models.CharField(max_length=20, verbose_name="Номер Телефона")
    whatsapp = models.CharField(max_length=200, blank=True, verbose_name="Whatsapp")
    telegram = models.CharField(max_length=200, blank=True, verbose_name="Telegram")
    instagram = models.CharField(max_length=55, verbose_name="Instagram")
    twitter = models.CharField(max_length=55, verbose_name="Twitter")
    facebook = models.CharField(max_length=55, verbose_name="Facebook")

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return self.phone_number


class Mentor(models.Model):
    specialty = models.CharField(max_length=255, verbose_name="Специальность")
    name = models.CharField(max_length=255, verbose_name="Ф.И.О")
    description = models.TextField(null=True, verbose_name="Описание")
    image = models.ImageField(upload_to="mentor", null=True, blank=True, verbose_name="Изображение")

    class Meta:
        verbose_name = 'Ментора'
        verbose_name_plural = 'Менторы'

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок", null=True)
    description = models.TextField(null=True, verbose_name="Описание")
    mentor = models.ForeignKey(
        to=Mentor,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    age = models.CharField(max_length=255, null=True, verbose_name="Возраст")
    time = models.CharField(max_length=15, null=True, verbose_name="Продолжительность Занятия")
    image = models.ImageField(verbose_name='Изображение', upload_to="course", null=True, blank=True, )

    duration = models.IntegerField(default=0, choices=(

        (1, '1 месяц'),
        (2, '2 месяц'),
        (3, '3 месяц'),
        (4, '4 месяц'),
        (5, '5 месяц'),
        (6, '6 месяц'),
    ), verbose_name="Длительность Курсов")
    price = models.IntegerField(null=True, blank=True, verbose_name="Цена")

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return self.title

class CourseImage(models.Model):

    title = models.CharField(verbose_name='Заголовок', max_length=255, null=True)
    images = models.ImageField(upload_to='course1', verbose_name='Изображение')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='images')

    class Meta:
        verbose_name = 'Изображение (Курсы)'
        verbose_name_plural = 'Изображении (Курсы)'

    def __str__(self):
        return self.title


class Application(models.Model):
    name = models.CharField(max_length=255, verbose_name="Ф.И.О")
    mail = models.CharField(max_length=255, verbose_name="Почта")
    phone_number = models.CharField(max_length=20, verbose_name="Номер Телефона")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время Заявки")

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return self.phone_number


class Feedback(models.Model):
    name = models.CharField(max_length=255, verbose_name="Ф.И.О")
    image = models.ImageField(upload_to="feedback", null=True, blank=True, verbose_name="Изображение")
    message = models.TextField(null=False, verbose_name="Текст")
    phone_number = models.CharField(max_length=20, verbose_name="Номер Телефона")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок", null=True)
    description = models.TextField(null=False, verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True)
    date = models.CharField(max_length=255, verbose_name="Дата Провождения Мероприятия")
    location = models.CharField(max_length=255, verbose_name="Место Мероприятия")
    image = models.ImageField(upload_to="event", null=True, blank=True, verbose_name="Изображение")

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = "Мероприятия"

    def __str__(self):
        return self.title


class FAQ(models.Model):
    question = models.TextField(null=True, verbose_name="Вопрос")
    answer = models.TextField(null=True, verbose_name="Ответ")

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQ'

    def __str__(self):
        return self.question


class FAQCourse(models.Model):
    question = models.CharField(null=True, verbose_name='Вопрос', max_length=500)
    answer = models.CharField(null=True, verbose_name='Ответ', max_length=500)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='Курсы', null=True)

    class Meta:
        verbose_name = 'FAQ (Курс)'
        verbose_name_plural = 'FAQ (Курсы)'

    def __str__(self):
        return self.question
