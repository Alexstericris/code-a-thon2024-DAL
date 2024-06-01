from django.urls import path

from . import views

urlpatterns = [
    path("testemail", views.testmail, name="testemail"),
    path("testwrite", views.testwrite, name="testwrite"),
]