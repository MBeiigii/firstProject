from django.shortcuts import render, redirect
from django.contrib.auth.forms import (
    UserCreationForm, PasswordChangeForm,)
from django.urls import reverse_lazy
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, views as auth_views 
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse,HttpResponseBadRequest
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group
from pytz import timezone as Timezone
import logging
logger = logging.getLogger(__name__)
local_tz = Timezone('Asia/Tehran')

@login_required
def reset_password(request, username, new_password):
    # چک کردن وجود گروه 'respass' برای کاربر
    if request.user.groups.filter(name='respass').exists():
        # یافتن کاربر با نام کاربری
        User = get_user_model()
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return HttpResponseBadRequest('کاربر با این نام کاربری یافت نشد.')

        # اعتبارسنجی رمز عبور جدید
        try:
            validate_password(new_password, user)
        except ValidationError as e:
            return HttpResponseBadRequest(', '.join(e.messages))

        # تنظیم رمز عبور جدید
        user.password = make_password(new_password)
        user.save()

        return HttpResponse('رمز عبور با موفقیت تغییر یافت.')

    return HttpResponseBadRequest('شما اجازه تغییر رمز عبور را ندارید.')


def custom_login(request):
    if request.method == 'POST':
        # اعتبارسنجی ورود
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'خوش آمدید.')
            return redirect('myare:crt')  # تغییر به URL صفحه خانه شما
        else:
            messages.error(request, 'اطلاعات ورودی اشتباه است.')
    return render(request, 'account/login.html')

def custom_logout(request):
    logout(request)
    messages.info(request, 'خروج موفق')
    return redirect('account:login')  # تغییر به URL صفحه خانه شما


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account:login')
    else:
        form = UserCreationForm()
    return render(request, 'account/register.html', {'form': form})


@login_required
def changepassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'رمز عبور با موفقیت تغییر کرد.')
            return redirect('account:login')
        else:
            messages.error(request, 'خطا در تغییر رمز عبور.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'account/changepassword.html', {'form': form})

# def passwordreset(request):
#     return HttpResponse('ddd')

# ////////////////////////////


class UserPasswordResetView(auth_views.PasswordResetView):
    template_name = 'account/passwordreset.html'
    success_url = reverse_lazy('account:password_reset_done')
    email_template_name = 'account/passwordresetemail.html'


class UserPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = 'account/password_reset_confirm.html'
    success_url = reverse_lazy('account:password_reset_complete')

class UserPasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'account/password_reset_done.html'

class UserPasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = 'account/password_reset_complete.html'