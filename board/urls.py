from django.urls import path
from . import views

app_name = 'board'
urlpatterns = [
    path('', views.read, name='home'),
    path('create/', views.create, name='newarticle'),
    path('board/update/<int:pk>',views.update, name='update'),
    path('delete/<int:pk>',views.delete, name='delete'),
    
]
