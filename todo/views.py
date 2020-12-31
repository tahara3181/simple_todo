from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.views.generic import ListView, DetailView, DeleteView
from .models import TodoModel
from django.http import HttpResponse
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
