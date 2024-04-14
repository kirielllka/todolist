from django.urls import path
from todo.views import TodoDAO
urlpatterns = [
    path('', TodoDAO.index, name='todo-index'),

    #auth
    path('signup/', TodoDAO.sign_up, name='todo-signup'),
    path('login/', TodoDAO.log_in, name='todo-login'),
    path('logout/', TodoDAO.log_out, name='todo-logout'),
    path('create_todo/', TodoDAO.Create_Todo, name='todo-create')
]