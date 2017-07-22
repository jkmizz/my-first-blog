from django.shortcuts import render

def recipe_list(request):
    return render(request, 'blog/recipe_list.html', {})
# Create your views here.
