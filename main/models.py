from django.db import models
from django.utils import timezone


class SizeVariant(models.Model):
    size = models.CharField(max_length=20)

    def __str__(self):
        return self.size

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.CharField(max_length=20)
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    size = models.ForeignKey(SizeVariant, on_delete=models.PROTECT, null=True, blank=True)


    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.product_name


class ProductImages(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.PROTECT)
    image = models.ImageField(upload_to='product_images')

    def __str__(self):
        if self.image:
            return self.image.url
        return ''