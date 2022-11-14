from . import views
from django.urls import path

urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('like/<slug:slug>', views.RecipeLike.as_view(), name='recipe_like'),
    path('recipes/add', views.AddRecipe.as_view(), name='add_recipe'),
    path('recipes/profile', views.Profile.as_view(), name='profile'),
    path('recipes/<int:pk>/update/', views.EditRecipe.as_view(), name='edit_recipe'),
    path('recipes/<int:pk>/delete/', views.DeleteRecipe.as_view(), name='delete_recipe'),
]