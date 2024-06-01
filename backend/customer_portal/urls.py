from django.urls import path

from . import views

urlpatterns = [
    path("getcompanies", views.getcompanies, name="getcompanies"),
]