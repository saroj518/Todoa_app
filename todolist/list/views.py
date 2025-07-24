from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from django.views.generic import ListView, DeleteView, UpdateView, CreateView, View
from django.urls import reverse_lazy
import requests


class Todolistview(ListView):
    
    model = Task
    template_name = 'list.html'
    context_object_name = 'task'


class TodoDeleteView(DeleteView): 
   model = Task
   template_name = 'delete.html'
   success_url = reverse_lazy("Todolistview")
   

class TodoUpdateview(UpdateView):
   model = Task
   template_name = 'update.html'
   fields = [ 'title']
   success_url = reverse_lazy("Todolistview")
    
class TodoCreateView(CreateView):
    model = Task
    template_name = 'create.html'
    fields = ['title']
    success_url = reverse_lazy("Todolistview")
    
class TodoDoneview(View):
    def post(self, request, pk):
       task = get_object_or_404(Task, pk=pk)
       task.is_done = not task.is_done
       task.save()
       return redirect(reverse_lazy('Todolistview'))
    




   
 
  
   