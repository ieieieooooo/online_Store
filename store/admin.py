from django.contrib import admin
from store import models

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('created_at',)

@admin.register(models.Storage)
class StorageAdmin(admin.ModelAdmin):
    list_display = ('amount',)

@admin.register(models.Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('street_address',)