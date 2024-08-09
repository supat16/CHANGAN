from django.contrib import admin
from .models import Employee, Position, Department, Status

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'manager', 'status', 'image', 'position', 'department')
    search_fields = ('name', 'address')
    list_filter = ('status', 'position', 'department')

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('name', 'salary')

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'manager')

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('name',)
