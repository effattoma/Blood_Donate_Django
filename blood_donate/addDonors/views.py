from django.http import HttpResponse
from django.shortcuts import render


def add_donor(request):
    return render(request, 'donor/_addDonor.html')
