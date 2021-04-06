from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .models import *

class ProductView(View):

    def get(self, request):
        products = Product.objects.all()
        
        return render(request, 'main.html', locals())


def modalproduct(request, pk):
    context = {}
    modal_product = get_object_or_404(Product, pk=pk)
    context['modal_product'] = modal_product
    return render(request, 'modal-product.html', context)


class GalleryView(View):

    def get(self, request):
        images = Gallery.objects.all()

        return render(request, 'gallery.html', locals())