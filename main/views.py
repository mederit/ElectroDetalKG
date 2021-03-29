from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .models import *

class ProductView(View):


    def get(self, request):
        products = Product.objects.all()
        return render(request, 'base.html', locals())

    # @property
    # def get_pk(self, request):
    #     products_pk = Product.objects.filter()
    #     img =
