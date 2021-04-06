from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField




class Product(models.Model):

    title = models.CharField(max_length=250, verbose_name='Наименование')
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')
    image = models.ImageField(upload_to='product_images', verbose_name='Изображение')
    description = models.TextField(verbose_name='Описания')
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title


class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery', verbose_name='Галерея')
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-created_at',)




