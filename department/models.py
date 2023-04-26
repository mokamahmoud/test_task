from django.db import models

# Create your models here.
class department(models.Model):
    code=models.AutoField(primary_key=True,editable=True
)
    name=models.CharField(max_length=200)
    
    def __str__(self):
        return self.name