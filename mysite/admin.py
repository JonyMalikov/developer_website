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


class ItemInline(admin.TabularInline):
    """Вывод инструментов в админке"""

    model = Item


class ServiceAdmin(admin.ModelAdmin):
    """Вывод видов сервиса в админке"""

    inlines = [ItemInline]


admin.site.register(Category)
admin.site.register(Testimony)
admin.site.register(Skill)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Author)
admin.site.register(Item)
admin.site.register(Message)
