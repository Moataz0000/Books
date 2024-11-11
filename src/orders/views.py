from django.shortcuts import render
from .forms import OrderBook
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .models import Order
from django.views.generic.edit import CreateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required



class RequestBook(CreateView):
    # decorators = [permission_required, login_required]
    
    
    model = Order
    fields = ['name','email', 'book']
    success_url = reverse_lazy('books:book_list')
    template_name = 'orders/order.html'
    
    # @method_decorator(decorators)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def form_valid(self, form):
        if not form.instance.name:
            error_message = "The name field is required."
            return render(self.request ,'errors.html', context={
                'error':error_message 
            })
        return super().form_valid(form)
        


