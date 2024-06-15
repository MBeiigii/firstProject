from django.urls import path
from django.contrib.auth import views as auth_views
from . import views



    
app_name = 'account'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.custom_login, name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('changepassword/', views.changepassword, name='changepassword'),
    path('passwordreset/', views.UserPasswordResetView.as_view(), name='passwordreset'),
    path('confirm/<uidb64>/<token>/', views.UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.UserPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('confirm/complete', views.UserPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('reset_password/<str:username>/<str:new_password>',views.reset_password,name='reset_password'),
    ]
   