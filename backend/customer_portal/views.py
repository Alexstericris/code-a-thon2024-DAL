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
    contracts = list(
        Contract.objects.prefetch_related('invoices').filter(companyID=request.GET.get('companyID')).all())
    serialized_contracts = []
    for contract in contracts:
        serialized_contract = {
            'contractName': contract.contractName,
            'contractTyp': contract.contractTyp,
            'contractLeasingCompany': contract.contractLeasingCompany,
            'companyID': contract.companyID,
            'contractStart': contract.contractStart,
            'contractRuntime': contract.contractRuntime,
            'contractEnd': contract.contractEnd,
            'contractRhythm': contract.contractRhythm,
            'contractPaymentType': contract.contractPaymentType,
            'contractInvestment': contract.contractInvestment,
            'contractDirectDebit': contract.contractDirectDebit,
            'assetID': contract.assetID,
            'invoices': [{
                'invoiceID': invoice.invoiceID,
                'invoiceDate': invoice.invoiceDate,
                'invoiceCosts': invoice.invoiceCosts,
                'invoiceStatus': invoice.invoiceStatus
            } for invoice in contract.invoices.all()]
        }
        serialized_contracts.append(serialized_contract)
    return JsonResponse(serialized_contracts, safe=False)

def getcontract(request):
    contracts = list(Contract.objects.filter(contractName=request.GET.get('contractName')).values())
    return JsonResponse(contracts, safe=False)
