from django.urls import path
from . import views
from .feeds import LatestPostsFeed



urlpatterns = [
    path('', views.ArticleList.as_view(), name='home'),
    path('<slug:slug>/', views.ArticleDetail.as_view(), name='article_detail'),
    path('upload/', views.image_upload_view, name='image_upload'),
    path("feed/rss", LatestPostsFeed(), name="post_feed"),

]