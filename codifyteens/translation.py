from modeltranslation.translator import register, TranslationOptions
from .models import AboutUs, Statistic, Course, Mentor, CourseStudyPlan, CourseProject, Feedback, FAQ, Event, \
    Certificate


@register(AboutUs)
class AboutUsTranslationOptions(TranslationOptions):
    fields = ('description', )
    required_languages = ('ru', 'en')


@register(Statistic)
class StatisticTranslationOptions(TranslationOptions):
    fields = ('description', )
    required_languages = ('ru', 'en')


@register(Course)
class CourseTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'text', 'duration', 'schedule', 'price')
    required_languages = ('ru', 'en')


@register(Mentor)
class MentorTranslationOptions(TranslationOptions):
    fields = ('first_name', 'last_name', 'description', )
    required_languages = ('ru', 'en')


@register(CourseStudyPlan)
class CourseStudyPlanTranslationOptions(TranslationOptions):
    fields = ('section', 'description',)
    required_languages = ('ru', 'en')


@register(CourseProject)
class CourseProjectTranslationOptions(TranslationOptions):
    fields = ('description',)
    required_languages = ('ru', 'en')


@register(Feedback)
class FeedbackTranslationOptions(TranslationOptions):
    fields = ('name', 'comment')
    required_languages = ('ru', 'en')


@register(FAQ)
class FAQTranslationOptions(TranslationOptions):
    fields = ('question', 'answer')
    required_languages = ('ru', 'en')


@register(Event)
class EventTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'location')
    required_languages = ('ru', 'en')


@register(Certificate)
class CertificateTranslationOptions(TranslationOptions):
    fields = ('name', )
    required_languages = ('ru', 'en')


