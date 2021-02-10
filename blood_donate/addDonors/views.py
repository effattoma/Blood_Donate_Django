from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages, auth
from django.contrib.auth.models import User




def add_donor(request):
    return render(request, 'donor/_addDonor.html')
