from django.contrib import admin
from .models import *


# Register your models here.
class AboutusAdmin(admin.ModelAdmin):
    class Meta:
        model = AboutUs

class CourseImageAdmin(admin.ModelAdmin):
  pass

class FAQCourseInline(admin.TabularInline):
  model = FAQCourse

class CourseImageInline(admin.StackedInline):
  model = CourseImage
  max_num=10
  extra=0


class CourseAdmin(admin.ModelAdmin):
  inlines = [CourseImageInline, FAQCourseInline]


class AboutUsImageAdmin(admin.ModelAdmin):
  pass

class AboutUsImageInline(admin.StackedInline):
  model = AboutUsImage
  max_num=10
  extra=0

class AboutUsAdmin(admin.ModelAdmin):
  inlines = [AboutUsImageInline, ]




models = [Advantages, Contact, Application, Feedback, Mentor, Event, FAQ, FAQCourse,]
admin.site.register(models)

admin.site.register(CourseImage, CourseImageAdmin)
admin.site.register(Course, CourseAdmin)

admin.site.register(AboutUsImage, AboutUsImageAdmin)
admin.site.register(AboutUs, AboutUsAdmin)


