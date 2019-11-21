from django.urls import path
from MyCompany import views

urlpatterns = [
    path('DeptList', views.DeptListFunc),
    path('EmpList', views.EmpListFunc),
    path('CustomerList', views.CustListFunc),
]