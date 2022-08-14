from django.shortcuts import render, redirect
from .models import Post,Category
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .forms import PostForm	
from django.views.generic import *
from django.urls import reverse_lazy
# Create your views here.

def rasm(request):
    category = request.GET.get('category')
    if category == None:
        post = Post.objects.all()

    else:
        post = Post.objects.filter(category__name=category)

    categories = Category.objects.all()
    
    context = {
        'posts':post[::-1],
        'categories':categories
        }

    return render(request,'projects/project.html',context)

def body(request,pk):
    body = Post.objects.get(id=pk)
    
    return render(request, 'projects/about.html',{'body':body})

def add_yangilik(request):
    form = PostForm
    if request.method =='POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request,'projects/add_yangilik.html',context)

class PostCreateView( CreateView ):
    model = Post
    template_name = 'projects/add_yangilik.html'
    fields = ['title','body','rasm','category']
    
class PostUpdateView(UpdateView):
    model = Post
    template_name = 'projects/post_edit.html'
    fields = ['title','body','rasm','category']
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'projects/post_delete.html'
    success_url = reverse_lazy('home')