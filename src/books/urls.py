from django.urls import path
from . import views



app_name = 'books'



urlpatterns = [
    path('', views.BookList.as_view(), name='book_list'),
    path('books/category/<slug:category_slug>/', views.BookList.as_view(), name="category"),
    path('book/<slug:slug>/', views.BookDetailView.as_view(), name='book_details'),
    path('book/<slug:slug>/edit/', views.BookEditView.as_view(), name='book_edit'),

]