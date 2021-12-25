from django.shortcuts import render

# Create your views here.
from django.views import generic
from .models import *
from .forms import *

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

def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance

            return render(request, 'article_detail.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'article_detail.html', {'form': form})