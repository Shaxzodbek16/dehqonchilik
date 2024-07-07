from django.contrib import admin
from .models import Product, Category, Store, News, Contact, Options


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'category', 'created_at')
    list_filter = ('title', 'category', 'created_at')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')
    search_fields = ('name', 'description', 'created_at')
    list_filter = ('name', 'description', 'created_at')


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'price', 'is_active')
    search_fields = ('name', 'description', 'created_at', 'price', 'is_active')
    list_filter = ('name', 'description', 'created_at', 'price', 'is_active')

    actions = ['activate_product_to_sell', 'deactivate_product_to_sell']

    def activate_product_to_sell(self, request, queryset):
        queryset.update(is_active=True)

    def deactivate_product_to_sell(self, request, queryset):
        queryset.update(is_active=False)

    activate_product_to_sell.short_description = "Sotuvga qo'yish"
    deactivate_product_to_sell.short_description = "Sotuvdan olish"


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at')
    search_fields = ('title', 'description', 'created_at')
    list_filter = ('title', 'description', 'created_at')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    main = ("name", "text", "telephone", "purpose", "created_at")
    list_display = main
    search_fields = main
    list_filter = main


@admin.register(Options)
class OptionsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')
    search_fields = ('name', 'description', 'created_at')
    list_filter = ('name', 'description', 'created_at')
