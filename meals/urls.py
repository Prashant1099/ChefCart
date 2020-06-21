from django.urls import path
from . import views

urlpatterns = [
    path('', views.mealList, name='meal-list'),
    path('<slug:slug>/', views.mealDetails, name='mealDetails'),
]