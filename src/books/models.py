from django.db import models
from django.contrib.auth.models import User





class Category(models.Model):
    title = models.CharField(max_length=255)
    slug  = models.SlugField(max_length=255, unique=True, db_index=True) 

    class Meta:
        verbose_name = 'Categorie'
        
    def __str__(self) -> str:
        return str(f'category-{self.title}')    
    
    



class Book(models.Model):
    name = models.CharField(max_length=300, help_text='300 character only.', db_index=True)
    slug = models.SlugField(max_length=300, unique=True, help_text='Ensure the slug is unique.', db_index=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True)
    author = models.ForeignKey(User, related_name='books', on_delete=models.CASCADE)
    overview = models.TextField()    
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-created']
        
    def __str__(self) -> str:
        return str(f'Book Of {self.author} - {self.name} ')    
    
    


    