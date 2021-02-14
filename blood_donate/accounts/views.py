from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.contrib.auth import get_user_model


def register(request):
    if request.method == "POST":
        method_dict = request.POST.copy()
        first_name = method_dict.get('first_name')
        last_name = method_dict.get('last_name')
        username = method_dict.get('username')
        email = method_dict.get('email')
        password = method_dict.get('password')
        password2 = method_dict.get('password2')
        get_mail = list(email)

        if password != password2:
            messages.error(request, 'Password does not match!!')
        elif password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists!')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists!')
                else:
                    obj = User.objects.create_user(
                        username=username,
                        password=password,
                        first_name=first_name,
                        last_name=last_name,
                        email=email
                    )
                    obj.save()
                    try:
                        subject = 'Registration'
                        message = "Mail from Donor:" + username + ""
                        email_from = settings.EMAIL_HOST_USER
                        send_mail(subject, message, email_from, [get_mail])
                        messages.success(request, 'Successfully Created Account  '
                                                  ' Thank You!')
                    except:
                        messages.error(request, 'Account Created but EMAIL is not confirm. ')

                    messages.success(request, 'Registration successfully completed!!!')
                    return HttpResponseRedirect(reverse('login'))

    return render(request, 'accounts/register.html')


def login(request):
    if request.method == "POST":
        method_dict = request.POST.copy()
        username = method_dict.get('username')
        password = method_dict.get('password')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Successfully Login!!!')
            return HttpResponseRedirect(reverse('adddonor'))
        else:
            messages.error(request, 'Invalid !!')
            return HttpResponseRedirect(reverse('login'))

    return render(request, 'accounts/login.html')
