from django.shortcuts import render,redirect
from Employee_app.forms import Object_Master,Employeeform
from django.contrib import messages
from . models import *

def home(request):

    data=Employee_Details.objects.all()
    return render(request,'Employee_app/index.html',{'index':data})


def login(request):
    return render(request,"Employee_app/login.html")

def register(request):
    form=Object_Master()
    if request.method=='POST':
        form=Object_Master(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Registration success you can now login now')
            return redirect('/login')
    return render(request,"Employee_app/reg.html",{'form':form})


def Add_Employee(request):
    form=Employeeform()
    if request.method=='POST':
        form=Employeeform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Employee successfull added")
            return redirect('/')

    return render(request,'Employee_app/Add_Employee.html',{'form':form})

def delete_record(request,id):
    trash=Employee_Details.objects.get(id=id)
    trash.delete()
    return redirect('/')




def update_record_2(request,id):
    item=Employee_Details.objects.get(id=id)
    
    item.Employeee_fname=request.POST['fname']
    item.Employeee_lname=request.POST['lname']
    item.Employeee_mail_id=request.POST['mailid']
    item.save()
    messages.success(request,"Updated successfully ")
    return redirect('/')



def update_record(request,id):
    modify=Employee_Details.objects.get(id=id)
    modify_2=Employee_Details.objects.all()
    context={
        'modify':modify,
        'modify_2':modify_2
    }
    return render(request,'Employee_app/update.html',context)


def view_button(request):
     data=Employee_Details.objects.all()
     return render(request,'Employee_app/view_button.html',{'view_button':data})

