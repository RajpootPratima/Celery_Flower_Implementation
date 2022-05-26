from django.urls import path
from app import views

urlpatterns = [
    path('fact/',views.CeleryCheck.as_view()),
]