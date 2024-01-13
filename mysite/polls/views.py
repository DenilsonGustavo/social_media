from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile


# Create your views here.
@login_required(login_url='signin')
def index(request):
    #return HttpResponse('<h1>Bem Vindo à Rede Social</h1>')
    return render(request,'index.html')

@login_required(login_url='signin')
def settings(request):
    return render(request, 'setting.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email já existe')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Nome já existe')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username,email=email, password=password)
                user.save()

                #log useri in and redict to settings page

                #create a Profile object for the new user

                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model,id_user=user_model.id)
                new_profile.save()
                return redirect('signup')
        else:
            messages.info(request, 'As senhas não sao iguais!')
            return redirect('signup')
    else:
        return render(request, 'signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,'Usuário ou senha inválidos')
            return redirect('signin')
    else:
        return render(request, 'signin.html')
@login_required(login_url='signin')
def logout(request):
    auth.logout(request)
    return redirect('signin')