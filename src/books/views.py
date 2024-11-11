from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Book, Category
from django.views.generic.edit import UpdateView
from .forms import UpdateBookForm
from django.urls import reverse_lazy





class BookList(ListView):
    """
    Display list of books & Categories.
    """
    
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'
    
    def get_queryset(self):
        category_slug = self.kwargs.get('category_slug')
        if category_slug:
            return Book.objects.filter(category__slug=category_slug)
        return Book.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all() 
        return context


    
    
class BookDetailView(DetailView):
    """
    Display Single Book.
    """
    
    model = Book
    template_name = 'books/book_details.html'
    context_object_name = 'book'
    
    



class BookEditView(UpdateView):
    """
    Update a book 
    """
    queryset = Book.objects.all().only('name', 'slug', 'author', 'overview', 'category')
    form_class = UpdateBookForm
    template_name = 'books/book_edit.html'
    
    def get_success_url(self):
        return reverse_lazy('books:book_details', kwargs={'slug':self.object.slug})
    

            
        