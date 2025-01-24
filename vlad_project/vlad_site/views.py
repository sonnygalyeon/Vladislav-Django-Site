from django.contrib.auth import login, authenticate
from django.shortcuts import redirect, render
from django.contrib import messages


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
    if request.method == 'POST':
        login_data = request.POST.get('login')
        password_data = request.POST.get('password')
        usr = authenticate(request, username=login_data, password=password_data)
        if usr is not None:
            login(request, usr)
            return redirect('')
        else:
            messages.success(request, 'Invalid username or password')
            return render(request, 'login.html')
    return render(request, 'login.html')


def register_view(request):
    # if request.method == 'POST':
    #     login_data = request.POST.get('login')
    #     password_data = request.POST.get('password')
    #     password_data2 = request.POST.get('password2')
    #     if password_data == password_data2:
    #         CustomUser.objects.create_user(login_data, password_data, password_data2)
    #         usr = authenticate(request, username=login_data, password=password_data)
    #
    #         if usr is not None:
    #             login(request, usr)
    #             return redirect('')
    #         else:
    #             return render(request, 'register.html')

    return render(request, 'register.html')


def python_about_view(request):
    return render(request, 'python-about.html')


def php_about_view(request):
    return render(request, 'php-about.html')


def csharp_about_view(request):
    return render(request, 'csharp-about.html')


def javascript_about_view(request):
    return render(request, 'js-about.html')


def java_about_view(request):
    return render(request, 'java-about.html')


def ruby_about_view(request):
    return render(request, 'ruby-about.html')


def html_about_view(request):
    return render(request, 'html-about.html')
