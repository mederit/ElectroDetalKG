from django.shortcuts import render
from django.views.generic import View

class ProductView(View):
    def get(self, request):
        return render(request, 'product/list.html')
