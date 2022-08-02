from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def user_login(request):
    if request.user.is_authenticated == True:
        return redirect('home:home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home:home')
        else:
            return render(request, 'accounts_app/error page.html')

    return render(request, 'accounts_app/login.html', {})


def user_logout(request):
    logout(request)
    return redirect('home:home')


def user_register(request):
    if request.user.is_authenticated == True:
        return redirect('home:home')
    context = {'errors': []}

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2:
            context['errors'].append('The passwords are not same')
            return render(request, "accounts_app/register.html", context)
            # if User.objects.get(username=username):
            #     context['errors'].append('This username is exists')
            #     return render(request, "accounts_app/register.html", context)

        User.objects.create(username=username, email=email, password=password1)

        return redirect('account:login')
    return render(request, "accounts_app/register.html", {})
