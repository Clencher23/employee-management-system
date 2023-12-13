from django.contrib import admin

from Employee.models import EmployeeDetails
from .models import *

# Register your models here.
admin.site.register(EmployeeDetails)
admin.site.register(EmployeeEducation)
admin.site.register(EmployeeExperience)
admin.site.register(hellouser)
