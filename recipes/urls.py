from django.urls import path

from recipes import views

# Create your views here.
urlpatterns = [
    path('', views.home),
    path('recipes/<int:id>/', views.recipe)
]

