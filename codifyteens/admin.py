from django.contrib import admin
from .models import AboutUs, Gallery, Statistic, Course, CourseStudyPlan, CourseProject, Application, Feedback, FAQ, \
    Event, Mentor

models = [AboutUs, Gallery, Statistic, Course, CourseStudyPlan, CourseProject, Application, Feedback, FAQ, Event,
          Mentor]
admin.site.register(models)
