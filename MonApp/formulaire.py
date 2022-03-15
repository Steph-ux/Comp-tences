from django import forms
from django.forms import ModelForm

from MonApp.models import Students


class StudentsForm(ModelForm):
    class Meta:
        model = Students
        fields = ['name', 'email', 'phone', 'adresse', 'image', 'cv','domaine', 'desc']
        labels = {'name':'Nom utilisateur','email':'Email','phone':'N°Téléphone','adresse':'Adresse','domaine':'Domaine','desc':'Description'}
        widgets = {'name':forms.TextInput(attrs={'class':'form-control'}),
                   'email': forms.TextInput(attrs={'class': 'form-control'}),
                   'phone': forms.NumberInput(attrs={'class': 'form-control'}),
                   'adresse': forms.TextInput(attrs={'class': 'form-control'}),
                   'domaine': forms.TextInput(attrs={'class': 'form-control'}),
                   'desc': forms.Textarea(attrs={'class': 'form-control','rows':5}),

                   }


class Login(forms.Form):
    username = forms.CharField(label="Nom utilisateur", widget=forms.TextInput(attrs={'class': 'form-control'}))
    pwd = forms.CharField(label="Mot de passe", widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class Register(forms.Form):
    username = forms.CharField(label="Nom utilisateur", widget=forms.TextInput(attrs={'class': 'form-control'}))
    pwd = forms.CharField(label="Mot de passe", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    pwd_confirm = forms.CharField(label="Mot de passe de confirmation", widget=forms.PasswordInput(attrs={'class': 'form-control'}))