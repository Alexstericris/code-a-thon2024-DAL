from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail


# Create your views here.

def testemail(request):
    #TODO NILS: sent email to receiver
    send_mail(
        "Subject here",
        "Here is the message.",
        "from@example.com",
        ["to@example.com"],
        fail_silently=False,
    )
    return HttpResponse("Email sent")