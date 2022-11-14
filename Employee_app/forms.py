from django.contrib.auth.forms import UserCreationForm
from .models import User,Employee_Details
from django import forms



class Object_Master(UserCreationForm):
    Firstname=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter user FirstName'}))
    Lastname=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter user LastName'}))
    Email=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Email Address'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter your Password'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Confirm password'}))
    class Meta:
        model=User
        fields=['Firstname','Lastname','Email','password1','password2']



class Employeeform(forms.ModelForm):
    class Meta:
         model=Employee_Details
         fields='__all__' 