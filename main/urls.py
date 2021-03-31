from django.urls import path
from .views import *

urlpatterns = [
    path('', ProductView.as_view()),
    path('<int:pk>/', modalproduct, name='modal-product'),
]