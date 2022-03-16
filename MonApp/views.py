from django import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from MonApp.formulaire import StudentsForm, Login, Register
from MonApp.models import Students


def dash(request):
    return render(request, 'dash.html')


def about(request):
    return render(request, 'about.html')


def listes(request):
    return render(request, 'listes.html', {'data': Students.objects.all()})


#def index(request):
#    if request.method == 'POST':
 #       form = StudentsForm(request.POST, request.FILES).save()
  #      return redirect('listes')
   # else:
    #    form = StudentsForm()
   # return render(request, 'index.html', {'form': form})


def details(request, id_voir):
    return render(request, 'details.html', {'voir': Students.objects.get(name=id_voir)})


def login_user(request):
    if request.method == 'POST':
        form = Login(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            pwd = form.cleaned_data['pwd']
            user = authenticate(username=username, password=pwd)
            if user is not None:
                login(request, user)
                return redirect('dash')
            else:
                messages.error(request, 'Connexion échouée')
                return render(request, 'login.html', {'form': form})
        else:
            for field in form.errors:
                form[field].field.widget.attrs['class'] += ' is-invalid'

            return render(request, 'login.html', {'form': form})
    else:
        form = Login()
        return render(request, 'login.html', {'form': form})


def register_user(request):
    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            pwd = form.cleaned_data['pwd']
            pwd_confirm = form.cleaned_data['pwd']
            user = User.objects.create_user(username=username, password=pwd)
            if user is not None:
                return redirect('login')
            else:
                messages.error(request, "Création de compte échouée")
                return render(request, 'register.html', {'form': form})
        else:
            return render(request, 'register.html', {'form': form})

        return render(request, 'register.html', {})

    form = Register()
    return render(request, 'register.html', {'form': form})


def clean(self):
    pwd = self.cleaned_data.get('pwd')
    pwd_confirm = self.cleaned_data.get('pwd_confirm')

    if pwd != pwd_confirm:
        raise forms.ValidationError("Les mots de passe ne sont pas identiques")

    return self.cleaned_data

def logout_user(request):
    logout(request)
    return redirect('login')


def search(request):
    query = request.GET["domaine"]
    liste_domaine = Students.objects.filter(domaine=query)
    return render(request, 'search.html', {'liste_domaine': liste_domaine})
