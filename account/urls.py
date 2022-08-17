from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import BaseRegisterView,IndexView
from .views import upgrade_me



urlpatterns = [

    path('login/',
         LoginView.as_view(template_name = 'account/login.html'),
         name='login'),
    path('logout/',
         LogoutView.as_view(template_name = 'account/logout.html'),
         name='logout'),
    path('signup/',
         BaseRegisterView.as_view(template_name = 'account/signup.html'),
         name='signup'),
    path('upgrade/', upgrade_me, name = 'upgrade'),
    path('personal/', IndexView.as_view(),name='personal account'),# Ссылка на обновление профиля
    # path('profile_update/',ProfileUpdateView.as_view(),name='profile_update'),
]