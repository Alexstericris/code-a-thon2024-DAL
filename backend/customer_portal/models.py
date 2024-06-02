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


class Users(models.Model):
    userID = models.CharField(max_length=200)
    userLastName = models.CharField(max_length=200)
    userFirstName = models.CharField(max_length=200)
    userEmail = models.CharField(max_length=200)
    userPhone = models.CharField(max_length=200)
    companyID = models.CharField(max_length=200)


class Assets(models.Model):
    assetID = models.CharField(max_length=200, unique=True)
    assetDescription = models.CharField(max_length=200)
    assetStreet = models.CharField(max_length=200)
    assetPLZ = models.CharField(max_length=200)
    assetTown = models.CharField(max_length=200)
    assetStatus = models.CharField(max_length=200)
    assetBuild = models.CharField(max_length=200)
    assetType = models.CharField(max_length=200)
    assetSubtenant = models.CharField(max_length=200)


class Contract(models.Model):
    contractName = models.CharField(max_length=200, unique=True)
    contractTyp = models.CharField(max_length=200)
    contractLeasingCompany = models.CharField(max_length=500)
    companyID = models.CharField(max_length=500)
    contractStart = models.CharField(max_length=200)
    contractRuntime = models.CharField(max_length=200)
    contractEnd = models.CharField(max_length=500)
    contractRhythm = models.CharField(max_length=200)
    contractPaymentType = models.CharField(max_length=200)
    contractInvestment = models.CharField(max_length=500)
    contractDirectDebit = models.CharField(max_length=200)
    assetID = models.ForeignKey(Assets, on_delete=models.CASCADE, db_column='assetID', to_field='assetID',
                                related_name='assets')


class Invoices(models.Model):
    invoiceID = models.CharField(max_length=200)
    invoiceDate = models.CharField(max_length=200)
    invoiceCosts = models.CharField(max_length=200)
    invoiceStatus = models.CharField(max_length=200)
    contractID = models.ForeignKey(Contract, on_delete=models.CASCADE, db_column='contractID', to_field='contractName',
                                   related_name='invoices')


class Event(models.Model):
    eventID = models.CharField(max_length=200)
    contractID = models.ForeignKey(Contract, on_delete=models.CASCADE, db_column='contractID', to_field='contractName',
                                   related_name='events')
    eventName = models.CharField(max_length=200)
    eventDate = models.CharField(max_length=200)


class Formular(models.Model):
    name = models.CharField(max_length=200)


class Message(models.Model):
    messageName = models.CharField(max_length=200)

# data fill
