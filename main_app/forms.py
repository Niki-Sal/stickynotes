from django import forms
from .models import Postit, Book

class PostitForm(forms.ModelForm):
  class Meta:
    model = Postit
    fields = ['index', 'content']


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('name', 'author', 'notetype', 'image')