from django.urls import path
from .views import TodoList, TodoDetail, TodoDelete

urlpatterns = [
    path('', TodoList.as_view(), name='list'),
    path('detail/<int:pk>', TodoDetail.as_view(), name='detail'),
    path('delete/<int:pk>', TodoDelete.as_view(), name='delete'),
]
