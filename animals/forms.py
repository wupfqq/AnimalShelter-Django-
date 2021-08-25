from django import forms
from .models import Animal,Curator,News
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

class MessForm(forms.Form):
    state = forms.CharField(label="Topic: ",widget=forms.TextInput(attrs={"class": "form-control", "autocomplete": "off"}))
    body = forms.CharField(label="Body: ",widget=forms.Textarea(attrs={"class": "form-control", "autocomplete": "off","rows":4}))



class SiteLogForm(AuthenticationForm):
    username = forms.CharField(label="User  name",widget=forms.TextInput(attrs={"class": "form-control", "autocomplete": "off"}))
    password = forms.CharField(label="Password",widget=forms.PasswordInput(attrs={"class": "form-control", "autocomplete": "off"}))

class RegisterForm(UserCreationForm):
    email=forms.EmailField(label="Email",widget=forms.EmailInput(attrs={"class": "form-control","autocomplete":"off"}))
    username=forms.CharField(label="User  name", widget=forms.TextInput(attrs={"class": "form-control","autocomplete":"off"}))
    password1 = forms.CharField(label="Password",widget= forms.PasswordInput(attrs={"class": "form-control","autocomplete":"off"}))
    password2 = forms.CharField(label="Confirm password", widget=forms.PasswordInput(attrs={"class": "form-control","autocomplete":"off"}))
    class Meta:
        model=User
        fields = ('username','email','password1','password2')


class AnimalForm(forms.ModelForm):
    class Meta:
        model=Animal
        fields = '__all__'
        widgets={
        'name':forms.TextInput(attrs={"class":"form-control"}),
        'gender':forms.TextInput(attrs={"class":"form-control"}),
        'age': forms.NumberInput(attrs={"class":"form-control"}),
        'appearence' :forms.Textarea(attrs={"class":"form-control"}),
        'description' :forms.Textarea(attrs={"class":"form-control"}),
       # 'photo': forms.ImageField(),
        'curator': forms.Select(attrs={"class":"form-control"}),
        'category': forms.Select(attrs={"class":"form-control"}),
        }

class CuratorForm(forms.ModelForm):
    class Meta:
        model=Curator
        fields = '__all__'
        widgets={
        'name':forms.TextInput(attrs={"class":"form-control"}),
        'description' :forms.Textarea(attrs={"class":"form-control"}),
        #'photo': forms.ImageField(),
        'organization': forms.Textarea(attrs={"class": "form-control"}),
        'addres': forms.Textarea(attrs={"class": "form-control"}),

        }

