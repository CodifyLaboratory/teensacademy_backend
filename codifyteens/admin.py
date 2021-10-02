from django.contrib import admin
from .models import AboutUs, Gallery, Statistic, Course, CourseStudyPlan, CourseProject, Application, Feedback, FAQ, \
    Event, Mentor, Certificate

models = [AboutUs, Gallery, Statistic, Course, CourseStudyPlan, CourseProject, Application, Feedback, FAQ, Event,
          Mentor, Certificate]
admin.site.register(models)
