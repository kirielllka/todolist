from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.template.response import TemplateResponse
from django.views import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from  django.db import IntegrityError
from django.contrib.auth import login, authenticate, logout
from django.utils.functional import SimpleLazyObject
from todo.forms import TodoForm
from todo.models import TodoModel

class TodoDAO(View):
    def sign_up(request:HttpRequest)->TemplateResponse:
        if request.method == 'GET':
            return render(request, 'todo/sign_up.html',context={'form': UserCreationForm})
        if request.method == 'POST':
            try:
                if request.POST['password1'] == request.POST['password2']:
                    user = User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
                    user.save()
                    login(request,user)
                    return redirect('todo-index')

                else:
                    
                    return render(request, 'todo/sign_up.html',context={'form': UserCreationForm, 'error':'Password is not'})
            except IntegrityError:
                return render(request, 'todo/sign_up.html',
                              context={'form': UserCreationForm, 'error': 'Its user already exsists'})

    def log_in(request:HttpRequest)->TemplateResponse:
        if request.method == 'GET':
            return render(request, 'todo/log_in.html', context={'form':AuthenticationForm})
        if request.method == 'POST':
            user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
            if user is None:
                return render(request, 'todo/log_in.html', context={'form':AuthenticationForm,'error':"This username or password doesnt exists"})
            else:
                login(request,user)
                return redirect('todo-index')

    def log_out(request:HttpRequest)->TemplateResponse:
        if request.method == 'POST':
            logout(request)
            return render(request, 'todo/index.html')
    def index(request:HttpRequest)->TemplateResponse:
        if request.user.pk == None:
            return render(request, 'todo/index.html')

        else:
            todos = TodoModel.objects.filter(user=request.user, complite_at__isnull=True)
            return render(request, 'todo/index.html', context={'todos':todos})

    def Create_Todo(request:HttpRequest)->TemplateResponse:
        if request.method == 'GET':
            return render(request, 'todo/create_Todo.html', context={'form':TodoForm})
        if request.method == 'POST':
            form = TodoForm(request.POST)
            newTodo = form.save(commit=False)
            newTodo.user = request.user
            newTodo.save()
            return redirect('todo-index')


