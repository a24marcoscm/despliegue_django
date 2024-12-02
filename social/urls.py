from django.urls import path, include
from . import views

app_name = 'social'

urlpatterns = [
    path('', views.homeSocial, name='homeSocial'),
    path('<int:page_id>/', views.pageSocial, name="pageSocial"),
    path('logout/', views.logout, name='logout'),
]
