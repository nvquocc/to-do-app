from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Todo


# Create your views here.
def list_view_todo(request):
    context = {'todo_list': Todo.objects.all()}
    return render(request, 'todo/todo_list.html', context)


def insert_to_do_item(request: HttpRequest):
    todo = Todo(content=request.POST['content'])
    todo.save()
    return redirect('/todos/list/')


def delete_to_do_item(request, todo_id):
    todo_delete = Todo.objects.get(id=todo_id)
    todo_delete.delete()
    return redirect('/todos/list/')
