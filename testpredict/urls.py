from django.urls import path

from . import views

app_name = "testpredict"

urlpatterns = [
    # ex: /testpredict/
    # textboxとbutton表示
    path('index/', views.index, name='index'),
    # 要検証
    path('post/new/', views.PostTodo, name='PostTodo'),
    path('post/todo/', views.todo, name='todo'),
    path("",views.top, name="top"),
    path("home/", views.home, name="home"),
    path('signup/',views.singnup, name='signup'),

]
