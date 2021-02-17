from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.conf import settings
from addDonors.models import DonorInfo


def add_donor(request):
    if request.method == 'POST':
        name = request.POST["name"]
        email = request.POST["email"]
        phone_Number = request.POST["phone_Number"]
        select_Blood_Group = request.POST["select_Blood_Group"]
        district = request.POST["district"]
        last_Donate_Date = request.POST["last_Donate_Date"]
        obj = DonorInfo.objects.create(name=name, email=email, phone_Number=phone_Number,
                                       select_Blood_Group=select_Blood_Group, district=district,
                                       last_Donate_Date=last_Donate_Date)
        obj.save()
        messages.success(request, 'Upload Successful')

        return render(request, 'donor/_addDonor.html')
    return render(request, 'donor/_addDonor.html')
