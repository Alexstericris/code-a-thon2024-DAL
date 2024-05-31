from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=200)

class BankDetails(models.Model):
    name = models.CharField(max_length=200)

class User(models.Model):
    email = models.CharField(max_length=200)

class Invoice(models.Model):
    name = models.CharField(max_length=200)

class Asset(models.Model):
    name = models.CharField(max_length=200)

class Contract(models.Model):
    name = models.CharField(max_length=200)

class Formular(models.Model):
    name = models.CharField(max_length=200)

class Message(models.Model):
    name = models.CharField(max_length=200)
