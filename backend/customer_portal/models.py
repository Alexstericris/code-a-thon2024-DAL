from django.db import models

class Company(models.Model):
    companyID = models.CharField(max_length=200)
    companyName = models.CharField(max_length=200)
    companyStreet = models.CharField(max_length=200)
    companyPLZ = models.CharField(max_length=200)
    companyTown = models.CharField(max_length=200)
    companyBranche = models.CharField(max_length=200)
    companyEmail = models.EmailField(max_length=200)
    companyPhone = models.CharField(max_length=200)
    companyTradingID = models.CharField(max_length=200)
    companyCourt = models.CharField(max_length=200)

class BankDetails(models.Model):
    name = models.CharField(max_length=200)

class Users(models.Model):
    email = models.CharField(max_length=200)

class Invoices(models.Model):
    name = models.CharField(max_length=200)

class Assets(models.Model):
    assetName = models.CharField(max_length=200)

class Contract(models.Model):
    name = models.CharField(max_length=200)
    asset = models.CharField(max_length=200)
    contractRuntime = models.CharField(max_length=500)
    contractChanges = models.CharField(max_length=1000)

class Formular(models.Model):
    name = models.CharField(max_length=200)

class Message(models.Model):
    name = models.CharField(max_length=200)

#data fill
