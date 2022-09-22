from django.urls import path
from .import views

urlpatterns = [
    path('', views.home),
    path('registrarEmpleados/', views.registrarEmpleados),
    path('editarEmpleado/<codigo>', views.editarEmpleado),
    path('edicionEmpleados/', views.edicionEmpleados),
    path('eliminarEmpleado/<codigo>', views.eliminarEmpleado)
]