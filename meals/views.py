from django.shortcuts import render
from .models import Meals, Category

def mealList(request):
    menuItems = Meals.objects.all()
    categories = Category.objects.all()

    context = {
        'menuItems': menuItems,
        'categories': categories
    }

    return render(request, 'meals/menu.html', context)

def mealDetails(request, slug):
    mealDetail = Meals.objects.get(slug=slug)

    context = {
        'mealDetail': mealDetail
    }

    return render(request, 'meals/mealDetails.html', context)