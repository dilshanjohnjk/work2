from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserRegisterForm(UserCreationForm):
    email =forms.EmailField()
    address = forms.CharField(max_length=255, required=False)
    contact_number = forms.CharField(max_length=20, required=False)
    img = forms.ImageField(required=False, help_text='Optional')
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)

    class Meta:
        model = User
        fields = ('username','first_name','last_name', 'email','img', 'password1', 'password2')