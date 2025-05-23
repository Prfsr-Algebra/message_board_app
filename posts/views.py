from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import posts
class HomePageView(ListView):
    model = posts
    template_name = 'home.html'
    context_object_name = 'all_post'