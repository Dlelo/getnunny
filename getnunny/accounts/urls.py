from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('nunnys/', views.nunnys),
    path('homeowner/', views.homeowner),
]