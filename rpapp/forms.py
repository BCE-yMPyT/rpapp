from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'author', 'created_date', 'published_date',
                  'picture', 'contract', 'rental_condition',)