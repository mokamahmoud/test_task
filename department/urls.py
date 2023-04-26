from django.urls import path
from . import views
from django.conf.urls import url
urlpatterns = [
    path('create',views.create,name="create"), 
    path('search',views.search,name="search"),
    path('edit',views.edit,name="edit"), 
    path('delete/<int:id>', views.delete, name='delete'),

]