from django.shortcuts import render
from post.models import CarPost
from category.models import Category

def home(request,category_slug=None):
    data=CarPost.objects.all()
    if category_slug is not None:
        category=Category.objects.get(slug=category_slug)
        data=CarPost.objects.filter(category=category)
        
    categories=Category.objects.all()

    return render(request,'home.html',{'data':data, 'category':categories})