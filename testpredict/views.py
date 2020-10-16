from django.shortcuts import render
from django.http import HttpResponse


from .NLP import helloworld
from .NLP import predict

# database
from testpredict.models import Taskclassification as task_class

# Create your views here.

def index(request):
    textpredict()
    return HttpResponse("index page")

def textpredict():
    
    print("test")
    helloworld.helloworld()
    entry = task_class.objects.get(pk=1)
    pred = predict.predict(entry.todo_text)
    print(pred)
    entry.todo_pred = pred
    entry.save()
    print(task_class.objects.get(pk=1).todo_pred)
    


