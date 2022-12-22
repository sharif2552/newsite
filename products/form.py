from django import forms
from django.forms import ModelForm
from .models import paymentmaking
from .models import info

class CustomerForm(ModelForm):
    class Meta:
        model = paymentmaking
        fields = '__all__'

class customerinfo(forms.ModelForm):
  class Meta:
    model = info
    fields = ["fullname", "mobile_number",]
    labels = {'fullname': "Name", "mobile_number": "Mobile Number",}