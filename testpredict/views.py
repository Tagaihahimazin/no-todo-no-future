from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from .NLP import helloworld
from .NLP import predict
from .NLP import train
from .NLP import retrain

# database
from testpredict.models import Taskclassification as task_class
#from testpredict.models import pred_db
#from testpredict.models import load_NLP
from .forms import TodoForm
from .forms import ChangeTodoForm
from django.contrib import messages

# Create your views here.
#def home(request):

@login_required
def TODOLIST(request):

  if request.method == 'POST':
      #form = ListForm(request.POST or None)
      form = TodoForm(request.POST or None)

      if form.is_valid():
        task=form.cleaned_data["item"]
        #all_items = List.objects.all
        all_items = task_class.objects.all
        messages.success(request, ('Item Has Been Added To List'))
        #return render(request, 'todoapp/home.html', {'all_items': all_items})

        #task=task_class.objects.get(pk=1)
        #task_item=task.item
        print(str(task))
        print("aaaaaaaaaaaaaaaaaaaaaaaaaa")
        print(all_items)
        pred = predict.predict(str(task),False)
        print(pred)

        q=task_class(item=task,todo_pred=pred,True_pred=pred)
        q.save()
        
        return render(request, 'testpredict/home2.html', {'all_items': all_items})
  else:
      #all_items = List.objects.all
      all_items = task_class.objects.all
      #return render(request, 'todoapp/home.html', {'all_items': all_items})
      return render(request, 'testpredict/home2.html', {'all_items': all_items})

def about(request):
  context = {'first_name': 'Kazufumi', 'last_name': 'Honda'}
  return render(request, 'testpredict/about.html', context)

def delete(request, list_id):
  #item = List.objects.get(pk=list_id)
  item = task_class.objects.get(pk=list_id)
  item.delete()

  messages.success(request, ('Item Has Been Deleted from List'))
  return redirect('testpredict:TODOLIST')


def uncomplete(request, list_id):
  #item = List.objects.get(pk=list_id)
  item = task_class.objects.get(pk=list_id)
  item.completed = False
  item.save()
  return redirect('testpredict:TODOLIST')

def complete(request, list_id):
  #item = List.objects.get(pk=list_id)
  item = task_class.objects.get(pk=list_id)
  item.completed = True
  item.save()
  return redirect('testpredict:TODOLIST')

def edit(request, list_id):
  #print(request.META)
  '''
  if request.method == 'POST':
    if 'item' in request.POST:
      #item = List.objects.get(pk=list_id)
      item = task_class.objects.get(pk=list_id)
      #form = ListForm(request.POST or None, instance=item)
      form = TodoForm(request.POST or None, instance=item)
    
      if form.is_valid() :
        form.save()
        #all_items = List.objects.all
        all_items = task_class.objects.all
        messages.success(request, ('Item Has Been Edited'))
        return redirect('testpredict:TODOLIST')

    if 'True_pred' in request.POST:

      #item = List.objects.get(pk=list_id)
      item = task_class.objects.get(pk=list_id)
      #form = ListForm(request.POST or None, instance=item)
      form = TodoForm(request.POST or None, instance=item)
    
      if form.is_valid() :
        form.save()
        #all_items = List.objects.all
        all_items = task_class.objects.all
        messages.success(request, ('Item Has Been Edited'))
        return redirect('testpredict:TODOLIST')
  '''
  if request.method == 'POST':
    #item = List.objects.get(pk=list_id)
    item = task_class.objects.get(pk=list_id)
    #form = ListForm(request.POST or None, instance=item)
    form = ChangeTodoForm(request.POST or None, instance=item)

    if form.is_valid():
      form.save()
      #all_items = List.objects.all
      all_items = task_class.objects.all
      messages.success(request, ('Item Has Been Edited'))

      #再学習
      retrain.retrain()

      return redirect('testpredict:TODOLIST')

    
  else:
    #item = List.objects.get(pk=list_id)
    item = task_class.objects.get(pk=list_id)
  
    print(item.True_pred)
    #return render(request, 'todoapp/edit.html', {'item': item})
    return render(request, 'testpredict/edit.html', {'item': item})

'''
def index(request):
    
    return PostTodo(request)
    #textpredict()
    #return HttpResponse("index page")

def todo(request):
    return HttpResponse("todo page")

def textpredict(todo_text):
    debug=False
    upload_debug=True

    print("test")
    #helloworld.helloworld()
    #entry = task_class.objects.get(pk=1)
    #entry = task_class.
    entry = task_class(todo_text=todo_text, todo_pred='other')
    if upload_debug:
        c,m=predict.load_model_file()
        predict.upload_db(c,m)

    pred = predict.predict(entry.todo_text,debug)
    entry.todo_pred = pred
    entry.save()

    print(task_class.objects.values_list('todo_text', flat=True))

    train.train()
    return pred

def PostTodo(request):
    #POST時処理
    if request.method == "POST":
        # Formのデータを用いTodoFormを再構築
        form = TodoForm(request.POST)
        # Formの値チェック
        if form.is_valid():
            return HttpResponse(textpredict(request.POST['todo_text']))
    # 初めてのアクセス
    else:
        print("!!!!!!!!!!!!!!!!!!!")
        # Formを新しくつくる
        form = TodoForm()

    return render(request, 'testpredict/todo.html', {'form': form})

'''
####ログイン処理

def top(request):
    return render(request,"testpredict/top.html")

@login_required
def home(request):
    return render(request,"testpredict/home.html")

def singnup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user_instance = form.save()
            login(request, user_instance)
            return redirect("testpredict:home")
    else:
        form = UserCreationForm()

    context = {
        "form":form
    }
    return render(request, 'testpredict/signup.html' , context)