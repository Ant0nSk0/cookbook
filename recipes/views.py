from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Recipe
from .forms import CommentForm

# Create your views here.


class RecipeList(generic.ListView):
    model = Recipe
    template_name = 'index.html'
    paginate_by = 6
    ordering = ['-created_on']


class RecipeDetail(View):

    def get(self, request, slug, *args, **kwargs):
        recipe = get_object_or_404(Recipe, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )