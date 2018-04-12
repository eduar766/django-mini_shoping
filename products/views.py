from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Category, Product

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'mini_shopping/index.html'
    context_object_name = 'product_list'

    def get_queryset(self):
        return Product.objects.order_by('-product_name')[:5]

class DetailView(generic.DetailView):
    model = Product
    template_name = 'mini_shopping/detail.html'


class CategoryView(generic.DetailView):
    model = Category
    template_name = 'mini_shopping/category.html'
