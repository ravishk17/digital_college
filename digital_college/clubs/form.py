from django import forms
from django.forms import ModelForm
from .models import Post, Images


class PostForm(ModelForm):
    subject = forms.CharField(widget=forms.TextInput(
        attrs={
            'id': 'subject1',
            'class': 'validate text-white', }
    ))

    content = forms.CharField(widget=forms.Textarea(
        attrs={
            'id': 'content',
            'placeholder': 'Write something here...',
            'style': 'height:100px;width:100%',
        }
    ))
    date = forms.DateTimeField(widget=forms.DateTimeInput(
        attrs={
            'id': 'date',
        }
    ))

    class Meta:
        model = Post
        fields = [
             'date', 'subject', 'content',
        ]


class ImageForm(ModelForm):
    image = forms.ImageField(widget=forms.FileInput(
        attrs={
            'type': 'file',
            'id': 'images'
        }
    ))

    class Meta:
        model = Images
        fields = [
             'image',
        ]
