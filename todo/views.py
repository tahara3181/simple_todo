from django.db import IntegrityError
from django.views.generic import ListView, DetailView, DeleteView, UpdateView
from .models import TodoModel
from django.urls import reverse_lazy


class TodoList(ListView):
    template_name = 'index.html'
    model = TodoModel


class TodoDetail(DetailView):
    template_name = 'detail.html'
    model = TodoModel


class TodoDelete(DeleteView):
    template_name = 'delete.html'
    model = TodoModel
    success_url = reverse_lazy('list')


class TodoUpdate(UpdateView):
    template_name = 'update.html'
    model = TodoModel
    fields = ('title', 'memo', 'duedate')
    success_url = reverse_lazy('list')
