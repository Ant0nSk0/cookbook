from django.shortcuts import render
from django.views import generic, View
from .models import Recipe

# Create your views here.


class RecipeList(generic.ListView):
    model = Recipe
    template_name = 'index.html'
    paginate_by = 6
    ordering = ['-created_on']
