from django.urls import path
from . import views

urlpatterns = [
    path('', views.adddonor, name='adddonor'),
    path('donor/', views.search_donor, name='donor'),
]
