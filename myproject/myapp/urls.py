from django.urls import path, re_path
from . import views

urlpatterns = [
    path('tasks/', views.task_list, name='task_list'),
]