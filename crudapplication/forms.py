from django import forms
from django.forms import fields, models
from crudapplication.models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model =Employee
        fields = "__all__"            #for all fields like eid ename etc...

        