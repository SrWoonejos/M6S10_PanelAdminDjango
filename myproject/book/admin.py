from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'autor', 'fecha_creacion', 'fecha_modificacion')
    search_fields = ('titulo', 'autor')
