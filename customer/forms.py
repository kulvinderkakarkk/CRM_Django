from django.contrib.auth.models import User
from django import forms
from .models import customers
from django.core.validators import RegexValidator

class CustomerRecords(forms.ModelForm):
    customer_name = forms.CharField(required=True, label="Customer Name", widget=forms.widgets.TextInput(attrs={'class':'form-control', 'placeholder':'Customer Name'}))
    customer_address = forms.CharField(required=True, label="Customer Address", widget=forms.widgets.TextInput(attrs={'class':'form-control', 'placeholder':'Customer Address'}))
    customer_email = forms.EmailField(required=True, label="Customer Email Address", widget=forms.widgets.TextInput(attrs={'class':'form-control', 'placeholder':'Customer Email Address'}))
    phone_number = forms.IntegerField(required=True, label="Phone Number", widget=forms.widgets.TextInput(attrs={'class':'form-control', 'placeholder':'Phone number'}), error_messages={"incomplete":"Please add a valid Phone number"}, validators=[RegexValidator(r"^[0-9]+$", "Enter a valid extension.")])
    state = forms.CharField(required=True, label="State", widget=forms.widgets.TextInput(attrs={'class':'form-control', 'placeholder':'State'}))
    country = forms.CharField(required=True, label="Country", widget=forms.widgets.TextInput(attrs={'class':'form-control', 'placeholder':'Country'}))

    class Meta:
        model=customers
        exclude=('last_updated_by',)