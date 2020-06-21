from django.shortcuts import render, redirect

from .forms import ContactForm, UserRegisterForm
from django.core.mail import send_mail
from django.http import HttpResponse
from Restaurant_Site.settings import EMAIL_HOST_USER
from django.contrib import messages

from meals.models import Meals, Category
from blog.models import Post
from offers.models import Offers

from django.contrib.auth import authenticate, login, logout


def home(request):
    menuItems = Meals.objects.all()
    categories = Category.objects.all()

    allPost = Post.objects.all()[:3]

    offersList = Offers.objects.all()



    #========================= User Register Form ============================
    registerForm = UserRegisterForm()

    if request.method == "POST":
        registerForm = UserRegisterForm(request.POST)

        if registerForm.is_valid():
            registerForm.save()
            user = registerForm.cleaned_data.get('username')
            messages.success(request, f'Account created for ' + user)
            return redirect('Home')
        else:
            messages.warning(request, 'Please enter valid values!')
            registerForm = UserRegisterForm()


    #========================= User Login Form ============================
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('Home')
        else:
            messages.warning(request, f'Please enter a valid Username or Password!')


    #===================== Contact-Us Form ============================
    if request.method == "POST":
        contactForm = ContactForm(request.POST)

        if contactForm.is_valid():            
            contactForm = ContactForm(request.POST)
            subject = 'Contact Us Alert!'
            message = 'Someone filled contact us form'
            reciepient = 'princepraa@gmail.com'
            send_mail(subject,message, EMAIL_HOST_USER, [reciepient], fail_silently = False)


            subject = 'Acknowledgement'
            message = 'Thanks for contacting us'
            reciepient = str(contactForm['email'].value())
            send_mail(subject, message, EMAIL_HOST_USER, [reciepient])

            contactForm.save()
            messages.success(request, f'Thanks for contacting us!')
            return redirect('/#section-contact')
    else:        
        contactForm = ContactForm()
    #===================== END Contact-Us Form ============================


    context = {
        'menuItems': menuItems,
        'categories': categories,
        
        'contactForm': contactForm,

        'allPost': allPost,

        'offersList': offersList,

        'registerForm': registerForm,
        
    }
    
    return render(request, 'home/home.html', context)


def logOut(request):
    logout(request)
    return redirect('Home')