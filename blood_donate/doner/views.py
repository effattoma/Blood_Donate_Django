from django.http import HttpResponse
from django.shortcuts import render


def donor(request):
    return render(request, 'donor/_searchDonor.html')
