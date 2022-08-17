from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from .models import Post
from django.forms import ModelForm
from django import forms


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'title', 'categoryType', 'postCategory', 'text']




# class CategoryForm(ModelForm):
#
#
#     class Meta:
#         model = Category
#         fields = ['name']