from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import messages
from addDonors.models import DonorInfo
from django.shortcuts import render


def adddonor(request):
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


def search_donor(request):
    SearchDonor = DonorInfo.objects.all()
    method_dict = request.GET.copy()
    district = method_dict.get('district') or None
    select_Blood_Group = method_dict.get('select_Blood_Group') or None

    if select_Blood_Group is not None:
        select_Blood_Group = method_dict['select_Blood_Group']
        SearchDonor = SearchDonor.filter(select_Blood_Group__iexact=select_Blood_Group)

    if district is not None:
        district = method_dict['district']
        SearchDonor = SearchDonor.filter(district__iexact=district)

    context = {
        'select_Blood_Group': select_Blood_Group,
        'district': district,
        'method_dict': method_dict,
        'SearchDonor': SearchDonor,
    }

    return render(request, 'donor/_searchDonor.html', context)
