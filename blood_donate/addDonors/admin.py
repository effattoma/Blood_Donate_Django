from django.contrib import admin
# Register your models here.
from addDonors.models import DonorInfo


class DonorAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_Number', 'select_Blood_Group', 'district', 'last_Donate_Date']
    search_fields = ['name', 'email', 'phone_Number', 'select_Blood_Group']


admin.site.register(DonorInfo, DonorAdmin)
