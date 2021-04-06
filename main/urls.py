from django.urls import path
from .views import *

urlpatterns = [
    path('', ProductView.as_view(), name='main'),
    path('<int:pk>/', modalproduct, name='modal-product'),
    path('gallery', GalleryView.as_view(), name='gallery-url'),
]