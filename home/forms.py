from django.forms import ModelForm
from .models import ContactUs

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ContactForm(ModelForm):
    class Meta:
        model = ContactUs
        fields = '__all__'
        


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']