from django import forms
from .models import Post, Arendator, Contract


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'address', 'author', 'created_date', 'published_date',
                  'picture', 'rental_condition',)

class ArendatorForm(forms.ModelForm):
    class Meta:
        model = Arendator
        fields = ('name', 'phone', 'email', 'photo',)

class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = ('rent_time_day', 'created_date', 'rent_finish_date',  'price_dollar',
                  'payment_by_contract_dollar','arendator', 'rent_obj','contract_file',
                  'rental_condition',)
