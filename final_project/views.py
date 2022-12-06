from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm
from django.urls import reverse_lazy



# Create your views here.
# def home(request):
#     return render(request, 'home.html', {})

# CLASS VIEW
class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-id']

    def get_context_data(self, *args, **kwargs):
        cat_meniu = Category.objects.all
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_meniu
        return context

def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats)
    return render(request,'categories.html', {'cats':cats, 'category_posts':category_posts})


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

    def get_context_data(self, *args, **kwargs):
        cat_meniu = Category.objects.all
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_meniu
        return context

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'
    # fields = ('title','body')

class AddCategoryView(CreateView):
    model = Category
    # form_class = PostForm
    template_name = 'add_category.html'
    fields = '__all__'
    # fields = ('title','body')
class UpdatePostView(UpdateView):
    model = Post
    template_name = 'update_post.html'
    fields = ['title', 'body']

class DeletePostView(DeleteView):
     model = Post
     template_name = 'delete_post.html'
     success_url = reverse_lazy('home')
