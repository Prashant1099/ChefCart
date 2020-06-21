from django.shortcuts import render
from .models import Offers


def offers(request):
    offersList = Offers.objects.all()

    context = {
        'offersList': offersList,
    }

    return render(request, 'offers/offers.html', context)
