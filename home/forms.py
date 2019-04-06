from django import forms
from home.models import Post

class HomeForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('post',)
    post= forms.CharField(required=True)