from django.db import IntegrityError
from django.views.generic import ListView
from .models import TodoModel



class TodoList(ListView):
    template_name = 'index.html'
    model = TodoModel
