from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('createEmployee',views.create,name="createEmployee"), 
    path('editEmployee',views.edit,name="editEmployee"), 
    path('deleteEmployee/<int:id>', views.delete, name='deleteEmployee'),
   path('searchEmployee', views.search, name='searchEmployee'),

]