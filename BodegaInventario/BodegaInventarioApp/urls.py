from django.urls import path

from BodegaInventarioApp import views

urlpatterns = [
    
    path('', views.inicio, name='Inicio'),
    path('mantenimiento/', views.mantenimiento, name='Mantenimiento'),
    path('transacciones/', views.transacciones, name='Transacciones'),
    path('inventario/', views.inventario, name='Inventario'),
    path('reportes/', views.reportes, name='Reportes'),
]