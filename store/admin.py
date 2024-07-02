from django.contrib import admin

# Register your models here.

from store.models import Size

from store.models import Brand

from store.models import Tag

from store.models import Category

from store.models import Product

admin.site.register(Product)

admin.site.register(Size)

admin.site.register(Brand)

admin.site.register(Tag)

admin.site.register(Category)