
from django import forms
from django.contrib.postgres.forms.array import SimpleArrayField

class product_posting_form(forms.Form):
    name = forms.CharField(max_length=200, required=True)
    description = forms.CharField(max_length=None, required=False)
    price = forms.IntegerField(required=True)
