from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('nunnys/', views.nunnys, name="products"),
    path ('homeownerslist', views.homeownerslist, name="homeownerslist"),
    path('homeowner/<str:pk_homeowner>/', views.homeowner, name="homeowner"),
    path('create_order/<str:pk_homeowner', views.createOrder, name="create_order"),
    path('update_order/<str:pk_order>/', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk_order>/', views.deleteOrder, name="delete_order")
]