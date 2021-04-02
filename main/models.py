from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


CATEGORY = (
    ('трансформатор', 'трансформатор'),
    ('столба: 11м', 'столба: 11м'),
    ('столба: 9м', 'столба: 9м'),
)

class Product(models.Model):

    title = models.CharField(choices=CATEGORY, default='', max_length=250, verbose_name='Наименование')
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')
    image = models.ImageField(upload_to='product_images', verbose_name='Изображение')
    description = models.TextField(verbose_name='Описания')
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title





    


