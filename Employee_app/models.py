from django.db import models
from django.contrib.auth.models import User



class Employee_Details(models.Model):
    Employeee_fname=models.CharField(max_length=150,null=False,blank=False)
    Employeee_lname=models.CharField(max_length=150,null=False,blank=False)
    Employeee_mail_id=models.CharField(max_length=150,null=False,blank=False)
   
    
   
    def __str__(self): 
        return self.Employeee_fname

    
