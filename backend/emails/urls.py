from django.urls import path

from . import views

urlpatterns = [
    path("testemail", views.testemail, name="testemail"),
]