from django.contrib import admin

# Register your models here.
from .models import  Category, Merch, Product, CartItem

class MerchAdmin(admin.ModelAdmin):
    list_display = ["name",]
    search_fields = ["name",]
    #list_filter = []
    #readonly_fields = ["quantity",]
 
    class Meta:
        model = Merch

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name",]
    search_fields = ["name",]
    #list_filter = []
    #readonly_fields = ["quantity",]
 
    class Meta:
        model = Category

class ProductAdmin(admin.ModelAdmin):
    list_display = ["image_tag", "name", "price", "merch", "category",]
    search_fields = ["name", "price", "merch__name", "category__name",]
    list_filter = ["merch", "category", "price"]
    #readonly_fields = ["quantity",]
 
    class Meta:
        model = Product

admin.site.register(Merch, MerchAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(CartItem)

