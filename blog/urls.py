from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
    path('detail/<slug:slug>', views.article_detail, name='article_detail'),
    path('list', views.article_list, name='articles_list'),
    path('category/<int:pk>', views.category_detail, name="category_detail"),
    path('search/', views.search, name="search_articles"),
    path('contact_us/', views.contactus, name="contact_us"),
    path('like/<slug:slug>/<int:pk>', views.like, name="like"),
    # path('detail/<slug:slug>', views.ArticleDetailView.as_view(), name='article_detail'),
]