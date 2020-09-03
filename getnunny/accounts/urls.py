from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('nunnys/', views.nunnys, name="products"),
    path('homeowner/<str:pk_homeowner>/', views.homeowner, name="customer"),
    path('creat_order', views.createOrder, name="create_order")
]