from django.urls import path
from . import views


urlpatterns = [
    path('', views.supertype_list),
    path('<int:pk>', views.super_types_list),
]