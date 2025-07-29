from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from . import views
from users import views as user_views

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("dashboard/", views.dashboard, name="dashboard"),
    path('profile/', user_views.profile, name='profile'),    
    path("register/", views.register, name="sign_up"),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
]