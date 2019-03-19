from django.contrib import admin
from readinghub.models import Category, Book, Event

class CategoryAdmin(admin.ModelAdmin):
    prepolulated_fields = {'slug':('name',)}

admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Event)

