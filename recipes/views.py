from django.shortcuts import render

def home(request):
    return render(request, 'recipes/pages/home.html')

def recipe(request, id):
    print(id)
    return render(request, 'recipes/pages/home.html')