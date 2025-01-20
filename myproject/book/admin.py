from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'autor', 'valoracion', 'fecha_creacion', 'fecha_modificacion')
    # Campos de solo lectura
    readonly_fields = ('fecha_creacion', 'fecha_modificacion')
    # Agregar filtros por valoración y fecha de modificación
    list_filter = ('valoracion', 'fecha_modificacion')
    search_fields = ('titulo', 'autor')
