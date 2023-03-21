from django.contrib import admin

from .models import userData, Employee

# Register your models here.
admin.site.register([
    userData,
    Employee
])
