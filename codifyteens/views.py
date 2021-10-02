from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from .models import AboutUs, Statistic, Course, Application, Feedback, FAQ, Event, Mentor, Certificate
from .serializers import AboutUsSerializer, StatisticSerializer, CourseListSerializer, CourseDetailSerializer, \
    MentorListSerializer, ApplicationDetailSerializer, FeedbackListSerializer, FAQListSerializer, EventListSerializer, \
    CertificatesListSerializer


class AboutUsViewSet(ReadOnlyModelViewSet):
    permission_classes = [AllowAny]
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer


class StatisticViewSet(ReadOnlyModelViewSet):
    permission_classes = [AllowAny]
    queryset = Statistic.objects.all()
    serializer_class = StatisticSerializer


class CourseViewSet(ReadOnlyModelViewSet):
    permission_classes = [AllowAny]
    queryset = Course.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return CourseListSerializer
        elif self.action == 'retrieve':
            return CourseDetailSerializer


class MentorViewSet(ReadOnlyModelViewSet):
    permission_classes = [AllowAny]
    queryset = Mentor.objects.all()
    serializer_class = MentorListSerializer


class ApplicationViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Application.objects.all()
    serializer_class = ApplicationDetailSerializer


class FeedbackViewSet(ReadOnlyModelViewSet):
    permission_classes = [AllowAny]
    queryset = Feedback.objects.all()
    serializer_class = FeedbackListSerializer


class FAQViewSet(ReadOnlyModelViewSet):
    permission_classes = [AllowAny]
    queryset = FAQ.objects.all()
    serializer_class = FAQListSerializer


class EventViewSet(ReadOnlyModelViewSet):
    permission_classes = [AllowAny]
    queryset = Event.objects.all()
    serializer_class = EventListSerializer


class CertificateViewSet(ReadOnlyModelViewSet):
    permission_classes = [AllowAny]
    queryset = Certificate.objects.all()
    serializer_class = CertificatesListSerializer