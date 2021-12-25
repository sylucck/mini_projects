from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
from .models import *

class ArticleAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    summernote_fields = ('content',)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}








  
admin.site.register(Article, ArticleAdmin)