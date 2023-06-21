from django.shortcuts import render
from .models import Dish

def home(request):
    return render(request, 'home.html')

def search_dish(request):
    query = request.GET.get('query')
    results = Dish.objects.filter(name__icontains=query)
    return render(request, 'search.html', {'results': results})
