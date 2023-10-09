from django.urls import path
from . import views

app_name = 'blogs'


urlpatterns = [
    path('', views.home_page, name="inicio"),
    path('post/<slug>', views.PostDetailView.as_view(), name="post_detalle"),
    path('featured/', views.FeaturedListView.as_view(), name="featured"),
    path('category/<slug:slug>', views.CategoryListView.as_view(), name="category"),
    path('search/', views.SearchResultView.as_view(), name="search"),

]
