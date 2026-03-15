from django.urls import path
from . import views_api

urlpatterns=[
    
     path('home/',
          views_api.get_home_data,
          name="api_home"),

     path('contact/',
          views_api.get_contact_data,
          name="api_contact"),

     path('services/', 
         views_api.get_service_list, 
         name='api_service_list'),

     path('services/<int:pk>/', 
         views_api.get_service_detail, 
         name='api_service_detail'),

    path('softwares/', 
        views_api.get_software_list, 
        name='api_software_list'),

    path('softwares/<int:pk>/', 
        views_api.get_software_detail, 
        name='api_software_detail'),

    path('hardwares/', 
        views_api.get_hardware_list, 
        name='api_hardware_list'),

    path('hardwares/<int:pk>/', 
        views_api.get_hardware_detail, 
        name='api_hardware_detail'),

    path('about/', 
        views_api.get_about_data, 
        name='api_about')]
