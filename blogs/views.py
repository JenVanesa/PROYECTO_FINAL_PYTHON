from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.utils import timezone
from blogs.models import Post, Categorias


# Create your views here.
def home_page(request):
   posts= Post.objects.all()
   categorias= Categorias.objects.all()
   featured = Post.objects.filter(featured= True)[:3]

   context = {
      'posts':posts,
      'categorias':categorias,  
      'destacados': featured 
   }
   return render (request, 'blogs/home_page.html', context=context)

class PostDetailView(generic.DetailView):
   model = Post
   query = Post.objects.filter(featured= True).filter(
         pub_date__lte= timezone.now()
   )

   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)   
      context['categorias'] = Categorias.objects.all()  
      return context
   
class FeaturedListView(generic.ListView):
   model = Post 
   template_name = 'blogs/featured_list.html'


   def get_queryset(self):
      query = Post.objects.filter(featured= True).filter(
         pub_date__lte= timezone.now()
      )

      return query
   
class CategoryListView(generic.ListView):
   model = Post 
   template_name = 'blogs/featured_list.html'

   def get_queryset(self):
      query = self.request.path.replace('categorias/', '')
      print(query)
      posts = Post.objects.filter(featured= True).filter(
         pub_date__lte= timezone.now()
      )
      
   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)   
      context['categorias'] = Categorias.objects.all()  
      return context