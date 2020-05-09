from django.shortcuts import render, redirect
from rest_framework.views import APIView
from .forms import TodoForm
from django.views import View
from .serializer import TodoListSerializer, TodoRetrieveSerializer
from rest_framework.response import Response
from .models import Todo
from django.contrib.auth.models import User
from rest_framework import status


class TodoCreateView(View):
    template_name = 'todo-create.html'

    def get(self, request):
        from pudb.remote import set_trace
        if request.user.is_authenticated:
            form = TodoForm(initial={'user': request.user})
            return render(request, self.template_name, dict(form=form))
        else:
            return redirect('user-login')


class TodoAPIView(APIView):
    def get(self, request):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            #return Response(serializer.data)
            #return Response(data=dict(status='Objeto creado'), status=status.HTTP_201_CREATED)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TodoRetrieveView(APIView):
    def get(self, request, id):
        try:
            instance = Todo.objects.get(id=id)
        except Todo.DoesNotExist:
            return Response({'Error, el objeto que busca no existe'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = TodoRetrieveSerializer(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)

    




