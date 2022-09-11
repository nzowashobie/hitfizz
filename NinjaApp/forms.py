# blog/forms.py
from NinjaApp.photo.models import Post
from photo.models import comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('name', 'comment')

    