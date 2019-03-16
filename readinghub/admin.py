from django.contrib import admin
from readinghub.models import Category, Book, Event

# Register your models here.

admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Event)

