from django.urls import path
from .views import HabitView

urlpatterns = [
    path('', HabitView.as_view()),
]