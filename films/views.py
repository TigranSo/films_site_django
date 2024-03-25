from django.shortcuts import render
from django.http import HttpResponse
from films.models import Films
from django.views.generic import ListView, DetailView, DeleteView


class FilmsListView(ListView):
    model = Films
    template_name = 'films/index.html'
    ordering = ["-time"]
    paginate_by = 6 
    context_object_name = 'films'
    
    
class FilmsDetailView(DetailView):
    model = Films
    template_name = 'films/film_detail.html' 