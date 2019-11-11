from django import forms
from django.contrib.auth.models import User
from .models import Dishes, Stores, Orders, SubmittedOrders, Roles, User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password', 'first_name', 'last_name')

class DishForm(forms.ModelForm):

    class Meta():
        model = Dishes
        fields = ('categary', 'photo_url', 'name', 'price')
