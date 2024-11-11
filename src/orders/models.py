from django.db import models

# Create your models here.




class Order(models.Model):
    name = models.CharField(max_length=20, blank=True) 
    email = models.EmailField()
    book = models.CharField(max_length=20)
    
    
    def __str__(self):
        return str(self.email)