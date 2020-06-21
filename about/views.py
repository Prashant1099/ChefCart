from django.shortcuts import render
from .models import About, WhyChooseUs, Chefs

def about(request):
    aboutUs = About.objects.all()
    whychooseus = WhyChooseUs.objects.all()
    chefs = Chefs.objects.all()

    context = {
        'aboutUs': aboutUs,
        'whychooseus': whychooseus,
        'chefs': chefs
    }

    return render(request, 'about/about.html', context)
