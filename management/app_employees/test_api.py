import os
from rest_framework.test import APITestCase
from rest_framework import status

class EmployeeTests(APITestCase):
    def test_create_employee(self):
        url = '/api/employees/'
        data = {
            "name": "John Doe",
            "address": "123 Main St",
            "manager": False,
            "status": 1,
            "position": 1,
            "department": 1
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_employees(self):
        url = '/api/employees/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
