from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.views.generic import ListView, DetailView
from .models import TodoModel
from django.http import HttpResponse


class TodoList(ListView):
    template_name = 'index.html'
    model = TodoModel


class TodoDetail(DetailView):
    template_name = 'detail.html'
    model = TodoModel
