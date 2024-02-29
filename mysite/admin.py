from django.contrib import admin

from .models import (
    Author,
    Category,
    Item,
    Message,
    Service,
    Skill,
    Testimony,
    Work,
)


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    """Вывод работ в админке"""

    list_display = ["title", "slug", "category"]
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Category, Testimony, Skill, Service, Author, Item, Message)
class ModelAdmin(admin.ModelAdmin):
    pass
