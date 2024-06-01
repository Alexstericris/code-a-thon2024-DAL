from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from customer_portal.models import Company, Contract
import json


# Create your views here.
def authcompany(request):
    print(request.body)
    body = json.loads(request.body)  # Python 3.6 and above

    company = list(Company.objects.filter(companyEmail=body['companyEmail']).values())[0]
    return JsonResponse(company, safe=False)


def getcompanies(request):
    companies = list(Company.objects.all().values())
    return JsonResponse(companies, safe=False)


def getcontracts(request):
    contracts = list(Contract.objects.filter(companyID=request.GET.get('companyID')).values())
    return JsonResponse(contracts, safe=False)

def getcontract(request):
    contracts = list(Contract.objects.filter(contractName=request.GET.get('contractName')).values())
    return JsonResponse(contracts, safe=False)
