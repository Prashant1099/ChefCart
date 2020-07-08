from django.shortcuts import render, redirect
from .forms import ReservationForm
from .models import Reservation
from django.core.mail import send_mail
from django.http import HttpResponse
from Restaurant_Site.settings import EMAIL_HOST_USER
from django.contrib import messages

def reservation(request):
    form = ReservationForm()

    if request.method == "POST":
        form = ReservationForm(request.POST)

        if form.is_valid():
            form.save()

            subject = 'Reservation Confirmation Acknowledgement'
            message = 'Your table has been successfully reserved. We look forward to host you soon.'
            reciepient = str(form['email'].value())
            send_mail(subject, message, EMAIL_HOST_USER, [reciepient], fail_silently=False)

            subject = 'New Reservation Alert'
            message = 'A new reservation has been done recently'
            send_mail(subject, message, EMAIL_HOST_USER, [EMAIL_HOST_USER], fail_silently=False)

            messages.success(request, f'Your table has been reserved successfully')
            return redirect('reservation')

    context = {
        'form': form
    }

    return render(request, 'reservation/reservation.html', context)
