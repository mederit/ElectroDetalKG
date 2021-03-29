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


#
# class ProductImages(models.Model):
#     product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='product_images')
#
#     def __str__(self):
#         if self.image:
#             return self.image.url
#         return ''


class Order(models.Model):
    cart_products = models.ForeignKey('CartProduct', on_delete=models.CASCADE, related_name='cart_products', blank=True, null=True)
    bay_product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='покупка товара',related_name='by_products', blank=True, null=True)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Обшая сумма')
    owner = models.CharField(max_length=255, verbose_name='Заказчик', unique=True)
    phone_number = PhoneNumberField(max_length=17, verbose_name='Контактный номер', unique=True)
    address = models.CharField(max_length=300, verbose_name='Адресс', unique=True)
    email_address = models.EmailField(verbose_name='адресс почты', unique=True)



class CartProduct(models.Model):
    products = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products')
    total_products = models.PositiveIntegerField(default=0, verbose_name='количество товара')
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Обшая сумма')


    


