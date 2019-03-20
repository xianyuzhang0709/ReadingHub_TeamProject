from django.contrib import admin
from readinghub.models import Category, Book, Event

class CategoryAdmin(admin.ModelAdmin):
    prepolulated_fields = {'slug':('name',)}

class BookAdmin(admin.ModelAdmin):
    prepolulated_fields = {'slug': ('title',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Event)

