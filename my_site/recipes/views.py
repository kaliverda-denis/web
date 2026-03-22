from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe
from .forms import RecipeForm
from django.contrib.auth.decorators import login_required

def home(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/home.html', {'recipes': recipes})

@login_required
def add_recipe(request):
    form = RecipeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'recipes/form.html', {'form': form})

@login_required
def edit_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    form = RecipeForm(request.POST or None, instance=recipe)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'recipes/form.html', {'form': form})

@login_required
def delete_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == "POST":
        recipe.delete()
        return redirect('/')
    return render(request, 'recipes/delete.html', {'recipe': recipe})