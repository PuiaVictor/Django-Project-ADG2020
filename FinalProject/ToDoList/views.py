from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoItem


def ToDoListView(request):
    all_todo_items = ToDoItem.objects.all()
    return render(request, 'ToDoList.html',
                  {'all_items': all_todo_items})


def addToDo(request):
    new_item = ToDoItem(content=request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/ToDoList/')


def deleteToDo(request, todo_id):
    item_to_delete = ToDoItem.objects.get(id=todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/ToDoList/')