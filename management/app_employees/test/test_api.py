import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from app_employees.models import Employee, Position, Department

@pytest.mark.django_db
def test_create_employee_api():
    client = APIClient()
    position = Position.objects.create(name="Software Engineer", salary=60000)
    department = Department.objects.create(name="Engineering")
    
    employee_data = {
        "name": "John Doe",
        "address": "123 Main St",
        "manager": True,
        "status": "Active",
        "position": position.id,
        "department": department.id
    }
    
    response = client.post(reverse('employee-list'), employee_data, format='json')
    
    assert response.status_code == status.HTTP_201_CREATED
    assert Employee.objects.count() == 1
    assert Employee.objects.get().name == "John Doe"

@pytest.mark.django_db
def test_employee_create(api_client, create_user):
    url = reverse('employee-list')
    position_obj = Position.objects.create(name='Developer', salary=60000)
    department_obj = Department.objects.create(name='IT', manager=None)
    
    data = {
        'name': 'Jane Smith',
        'address': '456 Elm St',
        'manager': True,
        'position': position_obj.id,
        'department': department_obj.id,
        'image': 'employee_images/IMG_20230817_201003.jpg'
    }
    response = api_client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['name'] == 'Jane Smith'

def test_get_employee_api(api_client, create_user, setup_data):
    employee = setup_data['employee']
    url = reverse('employee-detail', args=[employee.id])
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['name'] == employee.name

