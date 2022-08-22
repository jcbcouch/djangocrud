from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='list'),
    path('update_todo/<int:pk>/', views.updateTodo, name='update_todo'),
    path('delete/<int:pk>/', views.deleteTodo, name='delete')
]
