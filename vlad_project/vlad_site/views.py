from django.shortcuts import render


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


def login_view(request):
    return render(request, 'login.html')

def register_view(request):
    return render(request, 'register.html')