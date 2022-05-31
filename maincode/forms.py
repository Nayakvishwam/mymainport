from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class adddeatislofuser(forms.ModelForm):
        class Meta():
            model = mydata
            fields =['name','image','Collegename','Skills','email','Phonenumber','Address','age','media']
            widgets = {
            'name' : forms.TextInput(
                attrs={'class': 'appearance-none border-2 border-blue-600 focus:shadow-lg outline-none px-5 py-3 w-full', 'placeholder': 'Enter name', 'id': 'inputName'}),
            'Phonenumber' : forms.NumberInput(
                attrs={'class': 'appearance-none border-2 border-blue-600 focus:shadow-lg outline-none px-5 py-3 w-full', 'placeholder': 'Enter Phonenumber', 'id': 'inputSubject'}),
            'Collegename' : forms.TextInput(
                attrs={'class': 'appearance-none border-2 border-blue-600 focus:shadow-lg outline-none px-5 py-3 w-full', 'placeholder': 'Enter College name', 'id': 'inputSkill'}),

            'Skills' : forms.TextInput(
                attrs={'class': 'appearance-none border-2 border-blue-600 focus:shadow-lg outline-none px-5 py-3 w-full', 'placeholder': 'Enter Skills', 'id': 'inputCollege'}),
            'email' : forms.TextInput(attrs={
                                    'class': 'appearance-none border-2 border-blue-600 focus:shadow-lg outline-none px-5 py-3 w-full', 'placeholder': 'Enter Email', 'id': 'inputEmail'}),
            'Address' : forms.TextInput(
                attrs={'placeholder': 'Enter Address', 'class': 'appearance-none border-2 border-blue-600 focus:shadow-lg outline-none px-5 py-3 w-full', 'id': 'inputMessage', 'rows': 3}),
            'age' : forms.NumberInput(attrs={
                                    'class': 'appearance-none border-2 border-blue-600 focus:shadow-lg outline-none px-5 py-3 w-full', 'placeholder': 'Enter your age', 'id': 'basic-addon3'}),
            'media' : forms.FileInput(
                attrs={'class': 'appearance-none border-2 border-blue-600 focus:shadow-lg outline-none px-5 py-3 w-full', 'id': 'inputGroupFile02'}),
            'image':forms.FileInput(attrs={'class':'appearance-none border-2 border-blue-600 focus:shadow-lg outline-none px-5 py-3 w-full'})
            }