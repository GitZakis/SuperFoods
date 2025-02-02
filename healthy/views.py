import os
from django.conf import settings
from django.shortcuts import render,get_object_or_404,redirect
from django.template.defaulttags import comment
from .models import  Products,Categories,Manufacturers
from django.utils import timezone
from django.db.models import Q
import random

# Create your views here.
def post_list(request):
    cat = request.GET.get('cat')
    txt = request.GET.get('txt')

    if cat is None:
        if txt:
            product = Products.objects.filter(
                (Q(description__contains=txt) | Q(description__contains=txt)) & Q(published_date__lte=timezone.now())).order_by(
                'published_date')
        else:
            product = Products.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    elif cat.isdigit():
        cat = int(cat)
        product = Products.objects.filter(published_date__lte=timezone.now()).filter(category=cat).order_by('published_date')
    else:
        product = Products.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    return render(request, 'blog/post_list.html', {'products': product})


def post_detail(request, pk):
    products_detail = get_object_or_404(Products, pk=pk)
    return render(request, 'blog/post_detail.html', {'products_detail': products_detail})

