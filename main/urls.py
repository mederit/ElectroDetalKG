from django.urls import path
from .views import *

urlpatterns = [
    path('', ProductView.as_view(), name='main'),
    path('<int:pk>/', modalproduct, name='modal_product'),
]