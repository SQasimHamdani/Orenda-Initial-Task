from django import forms

from django.forms import ModelForm, TextInput, EmailInput
from employee.models import Employee, Department

class CreateEmployeeForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CreateEmployeeForm, self).__init__(*args, **kwargs)
        
    class Meta:
        model = Employee
        # fields = "__all__"
        fields = [  'name',
                'email',
                'cnic',
                'department',
                'image',
                ]