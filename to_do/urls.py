from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.list_view_todo),
    path('insert_todo/', views.insert_to_do_item, name='insert_to_do_item'),
    path('delete_todo/<int:todo_id>', views.delete_to_do_item, name='delete_to_do_item'),
]
