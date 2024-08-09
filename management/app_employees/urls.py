from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app_employees import views
from .views import EmployeeListCreateAPIView, PositionListCreateAPIView, DepartmentListCreateAPIView, StatusListCreateAPIView

urlpatterns = [
    path('employees/', EmployeeListCreateAPIView.as_view(), name='employee-list'),
    path('positions/', PositionListCreateAPIView.as_view(), name='position-list'),
    path('departments/', DepartmentListCreateAPIView.as_view(), name='department-list'),
    path('statuses/', StatusListCreateAPIView.as_view(), name='status-list'),
]
