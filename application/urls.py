from django.urls import path
from . import views

app_name = 'application'
urlpatterns = [
    path('app/', views.application, name='application'),
    path('newapplication/', views.applicationform, name='newapplication'),
    path('update/<int:pk>/', views.update, name='update'),  
]
