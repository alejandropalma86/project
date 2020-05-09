from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views import View
from django.contrib import messages

from django.views.generic import TemplateView
#from.models import workExperience, Education, Skills

class IndexView(TemplateView):
    template_name = 'index.html'


class RegisterView(View):
    def get(self, request):
        template_name = 'register.html'
        return render (request, template_name)

    def post(self, request):
        data = request.POST
        post_username = data.get('user_name', None) #Manera correcta de acceder a elementos del diccionario
        password = data.get('password', None)
        password2 = data.get('password_conf', None)
        if User.objects.filter(username=post_username).exists():
            messages.error(request, 'El usuario ya existe, intenta con otro nombre.')
            return redirect('register_a')
        if not password == password2:
            messages.error(request, 'Las contraseñas no son iguales')
            return redirect('register_a')
        else:
        
            user = User.objects.create(
                username=data['user_name'],
                email=data['email'],
                password=data['password'],
            )
            messages.success(request, 'Se ha creado con éxito')
            return redirect('home_a')


class LoginView(TemplateView):
    template_name = 'login.html'



