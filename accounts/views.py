from django.shortcuts import render,redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
import pyrebase
# Create your views here.
firebaseConfig = {
    "apiKey": "AIzaSyCF06Ain2piaGbL-LNfWMWwZj6990lkEmI",
    "authDomain": "cepmarketim-f0845.firebaseapp.com",
    "databaseURL": "https://cepmarketim-f0845.firebaseio.com",
    "projectId": "cepmarketim-f0845",
    "storageBucket": "cepmarketim-f0845.appspot.com",
    "messagingSenderId": "175820722510",
    "appId": "1:175820722510:web:8da5cae82acce4caf6ce1f"
  };
firebase=pyrebase.initialize_app(firebaseConfig)
auth=firebase.auth()

def login_view(request):
    form=LoginForm(request.POST or None)
    if form.is_valid():
        username=form.cleaned_data.get('username')
        password=form.cleaned_data.get('password')
        user=authenticate(username=username,password=password)
        login(request,user)
        return redirect('home')
    return render(request,'accounts/form.html',{'form':form, 'title':'Giriş Yap'})

def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        user1=form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user.set_password(password)
        # user.is_staff = user.is_superuser = True
        user.save()
        new_user = authenticate(username=user.username, password=password)
        kullanici_ekle=auth.create_user_with_email_and_password(user1,password)
        login(request, new_user)
        return redirect('home')

    return render(request, "accounts/form.html", {"form": form, 'title':'Üye Ol'})


def logout_view(request):
    logout(request)
    return redirect('home')
