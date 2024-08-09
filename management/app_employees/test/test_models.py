import pytest
from app_employees.models import Employee, Position, Department

@pytest.mark.django_db
def test_create_position():
    position = Position.objects.create(name="Software Engineer", salary=60000)
    assert position.name == "Software Engineer"
    assert position.salary == 60000

@pytest.mark.django_db
def test_create_department():
    department = Department.objects.create(name="Engineering")
    assert department.name == "Engineering"

@pytest.mark.django_db
def test_create_employee():
    position = Position.objects.create(name="Software Engineer", salary=60000)
    department = Department.objects.create(name="Engineering")
    employee = Employee.objects.create(name="John Doe", address="123 Main St", manager=True, status="Active", position=position, department=department)
    
    assert employee.name == "John Doe"
    assert employee.address == "123 Main St"
    assert employee.manager is True
    assert employee.status == "Active"
    assert employee.position == position
    assert employee.department == department
