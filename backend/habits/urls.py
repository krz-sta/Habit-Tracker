from django.urls import path
from .views import HabitView, HabitLogView, AllHabitLogsView

urlpatterns = [
    path('', HabitView.as_view()),
    path('<int:pk>/', HabitView.as_view()),
    path('<int:pk>/log/', HabitLogView.as_view()),
    path('<int:pk>/log/<int:log_pk>/', HabitLogView.as_view()),
    path('log/', AllHabitLogsView.as_view()),
]