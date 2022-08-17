from django_filters import FilterSet
from .models import Post,Category


class PostFilter(FilterSet):
       class Meta:
        model = Post
        fields = {
        'dateCreation': ['gt'],
         'postCategory':['exact'],
        }


class CategoryFilter(FilterSet):
       class Meta:
        model = Category
        fields = {
        'name': ['exact'],
        }