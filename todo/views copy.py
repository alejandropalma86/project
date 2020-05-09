from django.shortcuts import render, redirect
from django.views import View
from .forms import TodoForm



class TodoCreateView(View):
    template_name = 'todo-create.html'

    def get(self, request):
        #if request.user.is_authenticated:
            form = TodoForm(initial={'user': request.user})
            return render(request, self.template_name, dict(form=form))
        # else:
        #     return redirect('login_a')

    def post(self, request):
        data = request.POST
        form = TodoForm(data)
        if form.is_valid():
            form.save()
            messages.succes(request, 'Tarea creada con éxito')
            return redirect('create-todo')
        else:
            messages.error(request, 'Corrige los campos')
            return render(request, self.template_name, dict(form=form))

