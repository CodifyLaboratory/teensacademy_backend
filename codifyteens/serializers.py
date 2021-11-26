from rest_framework import serializers
from .models import AboutUs, Gallery, Statistic, Course, CourseStudyPlan, CourseProject, Feedback, FAQ, \
    Event, Mentor, Certificate


class GalleryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ('id', 'about_us', 'image')


class AboutUsSerializer(serializers.ModelSerializer):
    images = GalleryListSerializer(many=True, read_only=True)

    class Meta:
        model = AboutUs
        fields = ('id', 'description', 'images')


class StatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistic
        fields = ('id', 'number', 'description')


class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'title', 'description', 'age', 'image')


class MentorListSerializer(serializers.ModelSerializer):
    course = CourseListSerializer(many=False, read_only=True)

    class Meta:
        model = Mentor
        fields = ('id', 'course', 'first_name', 'last_name', 'description', 'image')


class CourseStudyPlanListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseStudyPlan
        fields = ('id', 'course', 'section', 'description')


class CourseProjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseProject
        fields = ('id', 'course', 'image', 'description')


class CourseDetailSerializer(serializers.ModelSerializer):
    mentors = MentorListSerializer(many=True, read_only=True)
    sections = CourseStudyPlanListSerializer(many=True, read_only=True)
    projects = CourseProjectListSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ('id', 'title', 'description', 'text', 'age', 'duration', 'schedule', 'price',
                  'mentors', 'sections', 'projects')


class FeedbackListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Feedback
        fields = ['id', 'name', 'image', 'comment', 'created_at']


class FAQListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ['id', 'question', 'answer']


class EventListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'date', 'time', 'location', 'image']


class CertificatesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ('id', 'name', 'image')