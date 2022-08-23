from django.urls import path
from .views import Notes

urlpatterns = [
    path('notes/', Notes.as_view()),
]