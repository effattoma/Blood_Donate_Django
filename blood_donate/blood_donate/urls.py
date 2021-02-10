
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('homes.urls')),
    path('about/', include('abouts.urls')),
    path('contact/', include('contacts.urls')),
    path('donor/', include('doner.urls')),
    path('add_donor/', include('addDonors.urls')),
    path('accounts', include('accounts.urls')),
    path('admin/', admin.site.urls),
]
