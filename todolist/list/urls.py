from django.urls import path
from . views import Todolistview, TodoDeleteView, TodoUpdateview, TodoCreateView, TodoDoneview
from . import views

urlpatterns = [
    path("", Todolistview.as_view(), name='Todolistview'),
    path('delete/<int:pk>/', TodoDeleteView.as_view(), name='todo_delete'),
    path('update/<int:pk>/', TodoUpdateview.as_view(), name='todo_update'),
    path('create/', TodoCreateView.as_view(), name='todo_create'),
    path('done/<int:pk>/', TodoDoneview.as_view(), name='todo_done'),
]




