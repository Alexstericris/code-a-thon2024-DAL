from django.urls import path

from . import views

urlpatterns = [
    path("authcompany", views.authcompany, name="authcompany"),
    path("getcompanies", views.getcompanies, name="getcompanies"),
    path("getcontracts", views.getcontracts, name="getcontracts"),
]