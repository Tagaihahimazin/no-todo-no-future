from django.urls import path

from . import views

urlpatterns = [
    # ex: /testpredict/
    # textboxとbutton表示
    path('', views.index, name='index'),
    # 要検証
    path('post/new/', views.PostTodo, name='PostTodo'),
    path('post/todo/', views.todo, name='todo'),
]
