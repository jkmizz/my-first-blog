from django.shortcuts import render
from django.utils import timezone
from .models import Recipe

def recipe_list(request):
	recipes = Recipe.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/recipe_list.html', {'recipes':recipes})
# Create your views here.


