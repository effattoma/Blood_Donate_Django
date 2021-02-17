from django.db import models
from django.http import HttpResponseRedirect
from django.conf import settings


class DonorInfo(models.Model):
    name = models.CharField(max_length=60, null=True, blank=True)
    email = models.CharField(max_length=60, null=True, blank=True)
    phone_Number = models.CharField(max_length=60, null=True, blank=True)
    select_Blood_Group = models.CharField(max_length=60, null=True, blank=True)
    district = models.CharField(max_length=60, null=True, blank=True)
    last_Donate_Date = models.CharField(max_length=60, null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-uploaded_at',)
