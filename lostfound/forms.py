from django import forms
from .models import Item, Claim

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['item_name', 'description', 'category', 'location', 'image']

class ClaimForm(forms.ModelForm):
    class Meta:
        model = Claim
        fields = ['phone_number', 'claim_description']
        widgets = {
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Phone Number'}),
            'claim_description': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
        }