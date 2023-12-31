from django.shortcuts import render
from django.views.generic import TemplateView, FormView, ListView
from .models import Post
# Create your views here.
class Home(ListView):
    http_method_names = ['get']
    template_name = 'index.html'
    model = Post
    context_object_name = 'posts'
    queryset = Post.objects.all().order_by('-id')[0:30]
