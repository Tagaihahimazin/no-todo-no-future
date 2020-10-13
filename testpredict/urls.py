from django.urls import path

from . import views

urlpatterns = [
    # ex: /testpredict/
    path('', views.index, name='index'),
]
