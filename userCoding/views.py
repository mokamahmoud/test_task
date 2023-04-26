from django.http import HttpResponseRedirect
from django.shortcuts import render
from pages.views import index
from .models import userCoding,department
from django.urls import reverse
from django.core.paginator import Paginator
from django.contrib import messages

#create employee whether have code from user  or auto increment from DB

def create(request):
    if request.method=="POST":
        user_code=request.POST['code']
        user_name=request.POST['name']
        mobile=request.POST['mobile']
        email=request.POST['email']
        birthdate=request.POST['birthdate']
        salary=request.POST['salary']
        department_name=request.POST['department_name']
        dep=department.objects.filter(name=department_name)
        if(dep):
           dep=department.objects.get(name=department_name)
           if(user_code):
                emp=userCoding.objects.create(user_code=user_code,user_name=user_name,
                                            mobile=mobile,email=email,birthdate=birthdate,salary=salary,department_id=dep.code)
                emp.save()
           else : 
            emp=userCoding.objects.create(user_name=user_name,mobile=mobile,email=email,birthdate=birthdate,salary=salary,department_id=dep.code)
            emp.save()
        else:  
            dep=department.objects.create(name=department_name)
            dep.save()
            dep=department.objects.get(name=department_name)
            if(user_code):
                emp=userCoding.objects.create(user_code=user_code,user_name=user_name,
                                            mobile=mobile,email=email,birthdate=birthdate,salary=salary,department_id=dep.code)
                emp.save()
            else : 
                emp=userCoding.objects.create(user_name=user_name,mobile=mobile,email=email,birthdate=birthdate,salary=salary,department_id=dep.code)
                emp.save()  
        messages.success(request,"created succsefully ")
        return HttpResponseRedirect(reverse(index))
    
 # edit employee  to edit employee 

def edit(request):
    if request.method=="POST":
        emp_code_id=request.POST['emp_code_id']
        user_code=request.POST['user_code']
        user_name=request.POST['user_name']
        mobile=request.POST['mobile']
        email=request.POST['email']
        birthdate=request.POST['birthdate']
        salary=request.POST['salary']
        department_name=request.POST['department_name']
        emp = userCoding.objects.get(user_code=emp_code_id)
        emp.delete() 
        dep=department.objects.filter(name=department_name)
        if(dep):
           dep=department.objects.get(name=department_name)
           emp=userCoding.objects.create(user_code=user_code,user_name=user_name,
                                           mobile=mobile,email=email,birthdate=birthdate,salary=salary,department_id=dep.code)
           emp.save()
        else:  
            dep=department.objects.create(name=department_name)
            dep.save()
            dep=department.objects.get(name=department_name)
            emp=userCoding.objects.create(user_code=user_code,user_name=user_name,
                                            mobile=mobile,email=email,birthdate=birthdate,salary=salary,department_id=dep.code)
            emp.save()
        
    return HttpResponseRedirect(reverse(index))

# delete employees
def delete(request, id):
  if request.method == 'POST':   
    emp = userCoding.objects.get(user_code=id)
    emp.delete()
  return HttpResponseRedirect(reverse(index))


#  employee search based on Employee name  or Employee id in  search value 
#  or using  showAll method to retrive all employes and thier departments

def search(request):
    if request.method == 'POST':
        emp_name = request.POST['empname']
        emp_id = request.POST['empid']
        if emp_id=="":
            emp_id=0
        querylist=userCoding.objects.all().order_by('user_code')
        deps=department.objects.all().order_by('code')
        paginator = Paginator(querylist, 3)
        page = request.GET.get('page')
        page_listings = paginator.get_page(page)
        paginator = Paginator(deps, 3)
        page = request.GET.get('page')
        page_departments = paginator.get_page(page)
        if (querylist):
            departments= set()
            if emp_name=="":
                 queryset = querylist.filter(user_code__exact=emp_id)
            else: 
                 queryset = querylist.filter(user_name__icontains=emp_name) | querylist.filter(user_code__exact=emp_id)
            for d in queryset:
             dep=department.objects.get(code=d.department_id)
             departments.add(dep.name)
             
            context={
              'em':queryset,
              'de':departments,
              'departments':deps,
              'employees':page_listings,
              'Deps':page_departments,
            }   
           
            return render(request,'pages/home.html',context)

        
    if request.method == 'GET':  
        userquerylist=userCoding.objects.all().order_by('user_code')
        paginator = Paginator(userquerylist, 3)
        page = request.GET.get('page')
        page_listings = paginator.get_page(page)
        deps=department.objects.all().order_by('code')
        paginator = Paginator(deps, 3)
        page = request.GET.get('page')
        page_departments = paginator.get_page(page)
        departments= set()
        
        for d in userquerylist:
             dep=department.objects.get(code=d.department_id)
             departments.add(dep.name)
        context={
              'em':userquerylist,
              'de':departments,
              'departments':deps,
              'employees':page_listings,
              'Deps':page_departments,
            }   
        
        return render(request,'pages/home.html',context)
