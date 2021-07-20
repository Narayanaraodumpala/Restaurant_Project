"""Restaurent_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include


from restarent_app import views

urlpatterns = [

    path('restarent_register/', views.restarent_register, name='restarent_register'),
    path('restarent_login/', views.restarent_login, name='restarent_login'),
    path('user_dashboard/', views.restaurent_dashboard, name='user_dashboard'),
    path('add_food/<int:pk>', views.add_food, name='add_food'),
    path('add_dish/', views.add_dish, name='add_dish'),
    path('restaurents/', views.restaurents, name='restaurents'),
    path('view_food/<str:pk>', views.view_food, name='view_food'),
    path('add_to_cart/<int:pk>', views.Add_to_cart.as_view(), name='add_to_cart'),
    path('view_cart/', views.View_cart.as_view(), name='view_cart'),
    path('order/<int:pk>', views.Order_cart.as_view(), name='order'),
    path('delete_item/<int:pk>', views.Delete_cart.as_view(), name='delete_cart'),
    path('order_item/', views.order_item, name='order_item'),
    path('view_promos/',views.View_promos.as_view(),name='view_offers'),
    path('veg/',views.veg,name='veg'),
    path('non_veg/',views.non_veg,name='non_veg'),
    path('chicken/',views.chicken,name='chicken'),
    path('muttun/',views.muttun,name='muttun'),
    path('fish/',views.fish,name='fish'),
    path('crabs/',views.crabs,name='crabs'),
    path('prawns/',views.prawns,name='prawns'),
    path('ice/',views.ice,name='ice'),
    path('colas/',views.colas,name='colas'),
    path('pizza/',views.pizza,name='pizza'),
    path('rest_view_food/<str:pk>',views.rest_view_food,name='rest_view_food'),
    path('edit_food_item/<int:pk>',views.edit_food,name='edit_food'),
    path('delete_food_item/<int:pk>',views.delete_food,name='delete_food'),
    path('save_rest_edit_info/<int:pk>',views.save_rest_edit_info,name='save_rest_edit_info'),
    path('edit_restaurent_info/<int:pk>',views.edit_restaurent_info,name='edit_restaurent_info'),
    path('save_rest_info/<int:pk>',views.save_rest_info,name='save_rest_info'),
    path('delete_restaurent/<int:pk>',views.delete_restaurent,name='delete_restaurent'),













]

