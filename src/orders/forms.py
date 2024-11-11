from django import forms




class OrderBook(forms.Form):
    Name = forms.CharField(max_length=200, required=True)
    Email = forms.EmailField(widget=forms.EmailInput(), help_text='enter your email here.')
    Book_Name = forms.CharField(max_length=20) 