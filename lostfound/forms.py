from django import forms
from .models import Item, Claim

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['item_name', 'description', 'category', 'location', 'image']