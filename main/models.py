from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


CATEGORY = (
    ('трансформатор', 'трансформатор'),
    ('бетон: 2.5', 'бетон: 2.5'),
    ('бетон: 1.5', 'бетон: 1.5'),
)

class Product(models.Model):
    created_by = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(choices=CATEGORY, default='', max_length=250, verbose_name='Наименование')
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')
    description = models.TextField(verbose_name='Описания')
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title


class ProductImages(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images')

    def __str__(self):
        if self.image:
            return self.image.url
        return ''