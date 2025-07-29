from django.urls import path
from . import views

urlpatterns = [
    path('', views.tour_list, name='tour_list'),
    path('request/<int:tour_id>/', views.make_request, name='make_request'),
    path('tours/', views.tour_list, name='tour_list'),

]