from django import forms
from django.forms.models import ModelForm

from .models import Contact, Comment


class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields="__all__"


class CommentForm(ModelForm):

    class Meta:
        model= Comment
        fields= ['body']
