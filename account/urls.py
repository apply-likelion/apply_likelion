from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'account'
urlpatterns = [
    path('passlist/',views.passed, name = 'passed'),
    path('acceptance/',views.mystate, name = 'acceptance'),
    path('detail/',views.detail, name = 'detail'),
    path('index/', views.index, name='index'),
    path('signin/', views.signin, name="signin"),
    path('account/', include('django.contrib.auth.urls')),
    path('logout/', views.logout, name="logout"),
    path('signup/', views.signup, name="signup"),
    
]
