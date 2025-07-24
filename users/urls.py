from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views
from users import views as user_views

urlpatterns = [
    path('profile/', user_views.profile, name='profile'),    
    path("register/", views.register, name="sign_up"),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
]