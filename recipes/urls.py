from django.urls import path

from recipes.views import home

# Create your views here.
urlpatterns = [
    path('', home),
]

