from django.shortcuts import render
from  django.http.response import HttpResponse
from blog.models import Blog ,Category
     
# Create your views here.
def index(request):
    context = {
        "blogs" :Blog.objects.all(),
        "categories":Category.objects.all()

    }
    #burada blog/index.html dememizin sebebi ilk olaarak templates klasorunun icindeki blog 
    #altindaki index.htmlleyi cagir demek istiyorum.
    return  render(request,"blog/index.html",context)
def blogs(request):
    context = {
        "blogs" :Blog.objects.filter(is_home="False"),
         "categories":Category.objects.all()

    }
    return  render(request, "blog/blogs.html", context)
def blogs_by_category(request,slug):
    context = {
        "blogs" :Blog.objects.filter(is_active=True,category__slug=slug),
         "categories":Category.objects.all(),
         "selected_category": slug

    }
    return  render(request, "blog/blogs.html", context)