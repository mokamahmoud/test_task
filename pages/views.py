from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from userCoding.models import userCoding
from department.models import department
from django.core.paginator import Paginator

# Create your views here.

# index function fisrtly rendred 

def index(request):
    
    employees=userCoding.objects.all().order_by('user_code')
    paginator = Paginator(employees, 3)
    page = request.GET.get('page')
    page_listings = paginator.get_page(page)
    
    departments=department.objects.all().order_by('code')
    paginator = Paginator(departments, 3)
    page = request.GET.get('page')
    page_departments = paginator.get_page(page)
    
    context={
       'employees':page_listings ,
       'Deps':page_departments,
       'departments':departments
       }
     
    return render (request,'pages/home.html',context) 

