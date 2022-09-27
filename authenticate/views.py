from django.shortcuts import render
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect(reverse("index"))

    if request.method == "POST":
        email= request.POST['email']
        password = request.POST['password']
        find_user = User.objects.filter(email=email).first()
        if(find_user):
            username= find_user.username
            user = authenticate(request, username=username, password=password)
            if user:
                auth_login(request, user)
                messages.success(request,"Login successful")
                return redirect('index')
            else:
                messages.warning(request,"Incorrect password")
        else:
            messages.warning(request,"No user found with this email address")
    context={}
    template= 'authenticate/login.html'
    return render(request, template, context)

def register(request):
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == 'POST':
        user= request.POST['username']
        email =request.POST['email']
        password =request.POST['password']
        password2= request.POST['password2']

        if ((user=='', email=='', password=='', password2=='')):
            if(password == password2):
                user=User.objects.create_user(
                    username=user,
                    email=email,
                    password=password
                )
                user.save()
                messages.success(request, "User created successfully")
                
    context={}
    template='authenticate/register.html'
    return render(request, template, context)
    
def logout(request):
    auth_logout(request)
    context={}
    template='authenticate/login.html'
    messages.warning(request, "Logout successfull")
    return render(request, template, context)