from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe
from .forms import RecipeForm

def home(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/home.html', {'recipes': recipes})


def add_recipe(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RecipeForm()
    return render(request, 'recipes/add_recipe.html', {'form': form})


def edit_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == "POST":
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'recipes/edit_recipe.html', {'form': form})


def delete_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == "POST":
        recipe.delete()
        return redirect('home')
    return render(request, 'recipes/delete_recipe.html', {'recipe': recipe})