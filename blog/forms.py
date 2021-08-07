from django import forms
from django.utils.translation import gettext, gettext_lazy as _
from .models import Post, ContactUs, Comment, Quote

class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ['title', 'slug', 'author', 'body', 'image', 'status']

    #labels = {'title':'Title','slug':'Slug', 'author':'Author', 'body':'Description', 'image':'Image', 'status':'Status'}
    #widgets = {'title':forms.TextInput(attrs={'class':'form-control'}),
    #'body':forms.Textarea(attrs={'class':'form-control'}), }"""

class EmailPostForm(forms.Form):
  name = forms.CharField(max_length=25)
  email = forms.EmailField()
  to = forms.EmailField()
  comments = forms.CharField(required=False, widget=forms.Textarea)


class CommentForm(forms.ModelForm):

  class Meta:
    model = Comment
    fields = ('name', 'email', 'body')


class ContactUsForm(forms.ModelForm):

  class Meta:
    model = ContactUs
    fields = ['name', 'email', 'address', 'message']

class QuoteForm(forms.ModelForm):

  class Meta:
    model = Quote
    fields = ['saying', 'say_by']