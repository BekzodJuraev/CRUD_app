from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy
from django.views import View
from .forms import MakeForm
from .models import CRUD
class CrudView(ListView):
    model=CRUD
    template_name = 'list_view.html'



class Create(CreateView):
    template_name='form_view.html'
    form_class=MakeForm
    success_url = reverse_lazy('home')


class Update(UpdateView):
    model = CRUD
    form_class = MakeForm
    template_name = 'updated_view.html'
    success_url = reverse_lazy('home')

class Delete(DeleteView):
    model = CRUD
    success_url = reverse_lazy("home")
    template_name = 'delete_view.html'







