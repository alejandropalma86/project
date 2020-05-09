from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views import View
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.utils import timezone
from .forms import RegisterForm, LoginForm, TodoDoneForm
from todo.views import TodoCreateView
from rest_framework.views import APIView
from django.views.generic import TemplateView
from .serializer import TodoUsersSerializer
from rest_framework.response import Response


class IndexView(View):
    template_name = 'index.html'
    
    def get(self, request):
        if request.user.is_authenticated:
            tareas_hechas = request.user.tudus.filter(done=True)
            tareas_no_hechas = request.user.tudus.filter(done=False)
            form = TodoDoneForm()
            form.fields['todos'].queryset = tareas_no_hechas
            return render(
                request, 
                self.template_name, 
                dict(tareas_hechas =tareas_hechas, tareas_no_hechas =tareas_no_hechas, form=form)
                )
        else: 
            return render(request, self.template_name, dict(form=LoginForm))


    def post(self, request):
        data = request.POST
        form = TodoDoneForm(data)
        if form.is_valid():
            cd = form.cleaned_data
            todo = cd.get('todos')
            todo.done = True
            todo.save()
            return redirect('home_a')

        else:
            messages.error(request, 'Lo sentimos algo salio mal')
            return redirect('home_a')



    

class RegisterView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home_a')
        template_name ='register.html'
        return render(request, template_name, dict(form=RegisterForm))

    def post(self, request):
        template_name = 'register.html'
        data = request.POST
        form = RegisterForm(data)
        if form.is_valid():
            cd = form.cleaned_data
            user = form.save()
            login(request, user)
            messages.success(request, 'Registro con éxito')
            return redirect('home_a')
        else:
            messages.error(request, 'Ingreso de datos incorrectos')
            for field in form.errors:
                form.fields[field].widget.attrs['class'] = 'input is-danger'

            return render(request, template_name, dict(form=form))


class LoginView(View):
    template_name = 'login.html'
    def get(self, request):
        return render(request, self.template_name, dict(form=LoginForm))

    def post(self, request):
        data = request.POST
        form = LoginForm(data)
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            #username = data.get('username', None)
            #password = data.get('password', None)
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home_a')
            
        messages.error(request, 'Usuario o contraseña incorrectos')
        return render(request, self.template_name, dict(form=form))

            
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home_a')

class TodoAPIViewUsers(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = TodoUsersSerializer(users, many=True)
        return Response(serializer.data)



