from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from flask import redirect
from django.core import serializers

from pages.views import index
from .models import department
from django.urls import reverse
from userCoding.models import userCoding 
from django.core.paginator import Paginator
from django.contrib import messages

# Create your views here.
import json

# department search based on deparment name search value 

def search(request):
    if request.method == 'POST':
        data = json.load(request)
        dep_name = data.get('searchValue')
        querylist=department.objects.all().values()
        if (querylist):
            queryset=querylist.filter(name__icontains=dep_name)          
            
            return JsonResponse({'context': list(queryset)})
       
    
# edit department  to edit department 
def edit(request):
    if request.method=="POST":
        code_id=request.POST['id']
        code=request.POST['code']
        name=request.POST['name']
        dep = department.objects.get(code=code_id)
        dep.delete()
        Dep=department.objects.create(code=code,name=name)
        Dep.save()
        
    return HttpResponseRedirect(reverse(index))

# delete department but only ifthe  department hasn't employss
def delete(request, id):
  if request.method == 'POST':
    emp=userCoding.objects.all().filter(department_id=id)  
    if(emp):
         messages.error(request,"sorry cannot delete beacause there is employees in department ")
    else:     
      dep = department.objects.get(code=id)
      dep.delete()
  return HttpResponseRedirect(reverse(index))


#create department whether have code from user  or auto increment from DB

def create(request):
    if request.method=="POST":
        code=request.POST['code']
        name=request.POST['name']
        if(code):
           Dep=department.objects.create(code=code,name=name)
           Dep.save()
        else : 
            Dep=department.objects.create(name=name)
            Dep.save()
        messages.success(request,"created succsefully ")
        return HttpResponseRedirect(reverse(index))

 