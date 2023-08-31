from django.urls import path
from rest_framework.routers import DefaultRouter
from education.apps import EducationConfig
from education.views import CourseViewSet, LessonListView, LessonDetailView, LessonCreateView, LessonUpdateView, \
    LessonDeleteView

app_name = EducationConfig

router = DefaultRouter()
router.register('course', CourseViewSet)

urlpatterns = [
                  path('', LessonListView.as_view()),
                  path('<int:pk>/', LessonDetailView.as_view()),
                  path('<int:pk>/update/', LessonCreateView.as_view()),
                  path('create/', LessonUpdateView.as_view()),
                  path('<int:pk>/delete/', LessonDeleteView.as_view()),

              ] + router.urls
