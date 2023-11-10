from django.contrib import admin
from .models import Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'year_of_release', 'genre', 'isbn', 'quantity', 'status')
    search_fields = ('title', 'author', 'isbn')

admin.site.register(Book, BookAdmin)
