from django import forms
from .models import Post, Arendator, Contract


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'address', 'author', 'created_date', 'published_date',
                  'picture', 'contract_file', 'rental_condition',)

class ArendatorForm(forms.ModelForm):
    class Meta:
        model = Arendator
        fields = ('name', 'photo',)

class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = ('rent_time', 'price', 'payment_by_contract', 'arendator', 'rent_obj',
                  'rental_condition',)
