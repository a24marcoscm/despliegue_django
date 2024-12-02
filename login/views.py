from django.shortcuts import render, redirect
from django.urls import reverse
from .models import User

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
            
            if(password == user.password):
                request.session['username'] = user.username
                return redirect(reverse('social:pageSocial', kwargs={'page_id': 0}))
            else:
                return render(request, "login/login.html", {'error': 'Contraseña incorrecta'})
        except User.DoesNotExist:
            return render(request, "login/login.html", {'error': 'Usuario no encontrado'})
    return render(request, "login/login.html")

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User(username=username, email=email, password=password)
        user.save()

        return redirect('login:login')
    return render(request, "login/register.html")