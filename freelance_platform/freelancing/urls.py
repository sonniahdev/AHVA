# freelancing/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.user_register, name='register.html'),
    path('login/', views.user_login, name='login.html'),
    path('profile/edit/', views.profile_edit, name='profile_edit.html'),
    path('work/request/submit/', views.work_request_submit, name='work_request_submit.html'),
]
