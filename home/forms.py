from django import forms
from home.models import Post

class HomeForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('post',)
    post= forms.CharField(required=True,widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Post Something !!'
        }
    ))