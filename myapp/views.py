from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, RosterUploadForm
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def home(request):
    return render(request, "home.html")

@login_required(login_url='login')
def checkers(request):
    return render(request, "checkers.html")

def registerPage(request):
    if request.user.is_authenticated: 
        return redirect('home')
    
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')

    context = {'form': form}
    return render(request, "register.html", context)

def loginPage(request):
    if request.user.is_authenticated: 
        return redirect('home')

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, "login.html", context)

@login_required(login_url='login')
def logOutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def fileCollectionPage(request):

    form = RosterUploadForm()

    if (request.method == "POST"):
        form = RosterUploadForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            form.user = form.request.user

            return redirect('home')

    context = {'form': form}
    return render(request, "filecollection.html", context)