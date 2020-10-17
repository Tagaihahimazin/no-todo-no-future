from django.urls import path

from . import views

app_name ="testpredict"

urlpatterns = [
    # ex: /testpredict/
    # textboxとbutton表示
    
    #path('index/', views.index, name='index'),
    # 要検証
    #path('post/new/', views.PostTodo, name='PostTodo'),
    #path('post/todo/', views.todo, name='todo'),
    
    #######################################
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('delete/<list_id>', views.delete, name='delete'),
    path('uncomplete/<list_id>', views.uncomplete, name="uncomplete"),
    path('complete/<list_id>', views.complete, name="complete"),
    path('edit/<list_id>', views.edit, name="edit"),
    #######################################
    path("",views.top, name="top"),
    ##touroku
    #path("home/", views.home, name="home"),
    path('signup/',views.singnup, name='signup'),

]
