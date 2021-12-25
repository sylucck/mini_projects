from django.shortcuts import render

# Create your views here.
from django.views import generic
from .models import *

class ArticleList(generic.ListView):
    model = Article
    
    context_object_name = 'artilce_list'
    template_name = 'index.html'
    def get_context_data(self,**Kwargs):
        #call the base implementation first to get the context
        context = super(ArticleList, self).get_context_data(**Kwargs)
        #Create any data and add it to the context
        context['article_list'] = Article.objects.filter(status=1).order_by('-created_on')

        return context
    
    

class ArticleDetail(generic.DetailView):
    model = Article
    template_name = 'article_detail.html'