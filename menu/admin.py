from django.contrib import admin

from .models import Food, FoodCategory


@admin.register(FoodCategory)
class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name_ru", "order_id")


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ("id", "name_ru", "category", "is_publish", "cost")
    list_filter = ("category", "is_publish")
    search_fields = ("name_ru",)
