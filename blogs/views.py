from django.shortcuts import render
from django.http import HttpResponse

from blogs.models import Post, Categorias


# Create your views here.
def home_page(request):
   posts= Post.objects.all()
   categorias= Categorias.objects.all()

   context = {
      'posts':posts,
      'categorias':categorias      
   }
   return render (request, 'blogs/home_page.html', context=context)

