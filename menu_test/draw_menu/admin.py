from django.contrib import admin
from .models import Menu, Item

# Register your models here.
class ItemInline(admin.StackedInline):
    extra = 1
    model = Item

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    fields = 'name',
    inlines = ItemInline,