from django.urls import path
from .views import AboutUsViewSet, StatisticViewSet, CourseViewSet, ApplicationViewSet, MentorViewSet, FeedbackViewSet, \
    FAQViewSet, EventViewSet

urlpatterns = [
    path('about-us/', AboutUsViewSet.as_view({'get': 'list'})),
    path('statistic/', StatisticViewSet.as_view({'get': 'list'})),
    path('feedbacks/', FeedbackViewSet.as_view({'get': 'list'})),
    path('questions/', FAQViewSet.as_view({'get': 'list'})),
    path('events/', EventViewSet.as_view({'get': 'list'})),

    path('mentors/', MentorViewSet.as_view({'get': 'list'})),

    path('application/', ApplicationViewSet.as_view({'post': 'create'})),

    path('courses/', CourseViewSet.as_view({'get': 'list'})),
    path('courses/<int:pk>/', CourseViewSet.as_view({'get': 'retrieve'})),
]