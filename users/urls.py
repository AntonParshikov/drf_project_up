from django.urls import path
from rest_framework.routers import DefaultRouter
from users.apps import UsersConfig
from users.views import UserListView, UserCreateView

app_name = UsersConfig.name


urlpatterns = [
                  path('user/', UserListView.as_view()),
                  # path('lesson/<int:pk>/', LessonDetailView.as_view()),
                  # path('lesson/update/<int:pk>/', LessonUpdateView.as_view()),
                  path('user/create/', UserCreateView.as_view()),
                  # path('lesson/delete/<int:pk>/', LessonDeleteView.as_view()),
                  # path('payment/', PaymentListView.as_view()),

              ]
