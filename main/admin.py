from django.contrib import admin

from .models import *


class ImageInlineAdmin(admin.TabularInline):
    model = ProductImages
    fields = ('image',)
    max_num = 5


@admin.register(Product)
class PostAdmin(admin.ModelAdmin):
    inlines = [ImageInlineAdmin,]
    # list_filter = ['created_by', 'created_at']


# admin.site.register(Product)
# admin.site.register(ProductImages)

