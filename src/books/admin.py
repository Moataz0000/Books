from django.contrib import admin
from .models import Category, Book

# Category Admin class
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)  
    list_filter = ('title',)  

# Book Admin class
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'created', 'slug')
    prepopulated_fields = {'slug': ('name',)}  
    search_fields = ('name', 'author__username')  
    list_filter = ('created', 'author')  
    date_hierarchy = 'created'  

admin.site.register(Category, CategoryAdmin)
admin.site.register(Book, BookAdmin)
