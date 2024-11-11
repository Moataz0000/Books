from django.urls import path
from .views import RequestBook



app_name = 'orders'


urlpatterns = [
    path('order-book/', RequestBook.as_view(), name='order-book')
]