#forms.py
from django import forms
from .models import Com_blog, Comment_album, Post
from photo.models import Comment
from ckeditor.widgets import CKEditorWidget
 
 
class CommentForm(forms.ModelForm):
  
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
        #fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Name','style': 'width:358px'}),
            'email': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Email','style': 'width:358px'}),
            'body': forms.Textarea(attrs={'class': 'form-control','placeholder': 'Comment'}),
        }
#album form
class Comm_Form(forms.ModelForm):
    class Meta:
        model = Comment_album
        fields = ('name', 'body')
        #fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Name','style': 'width:338px'}),
            'body': forms.Textarea(attrs={'class': 'form-control','placeholder': 'Comment'}),
        }

class Download_Form(forms.ModelForm):
    class Meta:
        model = Comment_album
        fields = ('name', 'body')
        #fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Name'}),
            'body': forms.Textarea(attrs={'class': 'form-control','placeholder': 'Comment'}),
        }

#post_detail form
class blog_Form(forms.ModelForm):
    class Meta:
        model = Com_blog
        fields = ('name', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Name','style': 'width:338px'}),
            'body': forms.Textarea(attrs={'class': 'form-control','placeholder': 'Comment'}),
        }

