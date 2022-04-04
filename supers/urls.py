from django.urls import path
from . import views


urlpatterns = [
    path('', views.super_list),
     path('<pk>/', views.super_list),
]