from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.utils import timezone
from django.db.models import Q


#import models
from .models import Post, Category


# Create your views here.
def home_page(request):
    posts = Post.objects.filter(pub_date__lte=timezone.now())
    categories = Category.objects.all()
    filter_featured = Post.objects.filter(features=True)[:3]

    context = {
        'posts': posts,
        'categories': categories,
        'filter_featured': filter_featured
    }

    return render(request, 'blogs/home_page.html', context=context)


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blogs/post_detail.html'
    queryset = Post.objects.filter(pub_date__lte=timezone.now())

    #aquie estan las consultas pero se creo el archivo context_processors.py

class FeaturedListView(generic.ListView):
    model = Post
    template_name = 'blogs/result.html'
    #paginacion
    paginate_by = 3

    def get_queryset(self):
        query = Post.objects.filter(features=True).filter(pub_date__lte=timezone.now())
        return query

    #aquie estan las consultas pero se creo el archivo context_processors.py

class CategoryListView(generic.ListView):
    model = Post
    template_name = 'blogs/result.html'
    paginate_by = 3

    def get_queryset(self):
        query = self.request.path.replace('/category/', '')
        print(query)
        post_list = Post.objects.filter(categories__slug=query).filter(
            pub_date__lte=timezone.now()
        )
        return post_list

    #aquie estan las consultas pero se creo el archivo context_processors.py


class SearchResultView(generic.ListView):
    model = Post
    template_name = 'blogs/result.html'
    paginate_by = 3

    def get_queryset(self):
        query = self.request.GET.get('search')
        post_list = Post.objects.filter(
            Q(title__icontains=query) | Q(categories__title__icontains=query)
        ).filter(
            pub_date__lte=timezone.now()
        ).distinct()
        return post_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('search')

        return context