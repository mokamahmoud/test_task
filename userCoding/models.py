from django.db import models
from department.models import department
class userCoding(models.Model):
    user_code=models.AutoField(primary_key=True,editable=True)
    user_name=models.CharField(max_length=200)
    mobile=models.CharField(max_length=50)
    email=models.EmailField(max_length = 254)
    birthdate=models.DateField()
    salary=models.CharField(max_length=100)
    department = models.ForeignKey(
        department,
        on_delete=models.CASCADE
    )
    def __str__(self):
        return self.user_name
    
    