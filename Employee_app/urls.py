
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('register', views.register,name='register'),
    path('Add_Employee', views.Add_Employee,name='Add_Employee'),
    path('delete_record/<id>',views.delete_record,name="delete_record"),
    path('update_record/<id>',views.update_record,name="update_record"),
    path('update_record_2/<id>',views.update_record_2,name="update_record_2"),
    path('view_button', views.view_button,name='view_button'),
]
