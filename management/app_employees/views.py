from rest_framework import generics
from .models import Employee, Position, Department, Status
from .serializers import EmployeeSerializer, PositionSerializer, DepartmentSerializer, StatusSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class EmployeeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_fields = ('position', 'department', 'status')
    ordering_fields = '__all__'
    ordering = ['name']  # Default ordering

class PositionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer

class DepartmentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class StatusListCreateAPIView(generics.ListCreateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
