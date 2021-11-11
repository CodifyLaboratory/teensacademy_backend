from django.contrib import admin
from .models import AboutUs, Gallery, Statistic, Course, CourseStudyPlan, CourseProject, Feedback, FAQ, \
    Event, Mentor, Certificate
from django.contrib.auth.models import Group, User


class GalleryInline(admin.StackedInline):
    model = Gallery
    fields = ('about_us', 'image')


class CourseStudyPlanInline(admin.StackedInline):
    model = CourseStudyPlan
    fields = ('course', 'section_ru', 'section_en', 'description_ru', 'description_en')


class CourseProjectInline(admin.StackedInline):
    model = CourseProject
    fields = ('course', 'description_ru', 'description_en', 'image')


class AboutUsAdmin(admin.ModelAdmin):
    model = AboutUs
    fieldsets = (
        ('Описание', {
            'fields': ('description_ru', 'description_en')
        }),
    )
    inlines = [GalleryInline]

class StatisticAdmin(admin.ModelAdmin):
    model = Statistic
    fieldsets = (
        ('Числовое значение', {
            'fields': ('number', )
        }),
        ('Описание', {
            'fields': ('description_ru', 'description_en')
        }),
    )


class CourseAdmin(admin.ModelAdmin):
    model = Course
    fieldsets = (
        ('Описание', {
            'fields': ('title_ru', 'title_en', 'description_ru', 'description_en', 'text_ru', 'text_en')
        }),
        ('Возрастная группа', {
            'fields': ('age', )
        }),
        ('Длителность', {
            'fields': ('duration_ru', 'duration_en')
        }),
        ('График', {
            'fields': ('schedule_ru', 'schedule_en')
        }),
        ('Стоимость', {
            'fields': ('price',)
        }),
        ('Изображение', {
            'fields': ('image',)
        }),
    )
    inlines = [CourseStudyPlanInline, CourseProjectInline]


class MentorAdmin(admin.ModelAdmin):
    model = Mentor
    fieldsets = (
        ('Курс', {
            'fields': ('course',)
        }),
        ('Личные данные', {
            'fields': ('first_name_ru', 'first_name_en', 'last_name_ru', 'last_name_en')
        }),
        ('Описание', {
            'fields': ('duration_ru', 'duration_en')
        }),
        ('Фотография', {
            'fields': ('image',)
        }),
    )


class FeedbackAdmin(admin.ModelAdmin):
    model = Feedback
    fieldsets = (
        ('Личные данные', {
            'fields': ('name_ru', 'name_en')
        }),
        ('Описание', {
            'fields': ('comment_ru', 'comment_en')
        }),
        ('Фотография', {
            'fields': ('image', )
        }),
    )


class FAQAdmin(admin.ModelAdmin):
    model = FAQ
    fieldsets = (
        ('Вопрос', {
            'fields': ('question_ru', 'question_en')
        }),
        ('Ответ', {
            'fields': ('answer_ru', 'answer_en')
        }),
    )


class EventAdmin(admin.ModelAdmin):
    model = Event
    fieldsets = (
        ('Описание', {
            'fields': ('title_ru', 'title_en', 'description_ru', 'description_en')
        }),
        ('Дата и время', {
            'fields': ('date', 'time')
        }),
        ('Адрес', {
            'fields': ('location_ru', 'location_en')
        }),
        ('Изображение', {
            'fields': ('image',)
        }),
    )


class CertificateAdmin(admin.ModelAdmin):
    model = Certificate
    fieldsets = (
        ('Название', {
            'fields': ('name_ru', 'name_en')
        }),
        ('Изображение', {
            'fields': ('image',)
        }),
    )


admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(Statistic, StatisticAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Mentor, MentorAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(FAQ, FAQAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Certificate, CertificateAdmin)

# admin.site.unregister(Group)