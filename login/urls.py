from django.urls import path, include
from . import views

app_name = 'login'

urlpatterns = [
    path('', views.login, name='login'),
    path('register', views.register, name="register")
]
