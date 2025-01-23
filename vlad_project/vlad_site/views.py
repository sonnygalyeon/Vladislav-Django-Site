from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def home(request):
    return render(request, 'home.html')


def about_page(request):
    return render(request, 'info_about.html')


def contact(request):
    return render(request, 'contact.html')


def profile(request):
    return render(request, 'profile.html')


def help_page(request):
    return render(request, 'help.html')


def themes_page(request):
    return render(request, 'themes.html')


def rules_of_use(request):
    return render(request, 'rules.html')


def login_view(request, user):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('')
    else:

        return redirect('login')


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            login_view(request, user)
    return render(request, 'register.html')
