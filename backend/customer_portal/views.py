from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from customer_portal.models import Company


# Create your views here.
def getcompanies(request):
    companies = list(Company.objects.all().values())
    return JsonResponse(companies, safe=False)
