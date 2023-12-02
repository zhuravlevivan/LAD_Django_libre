from django.contrib import admin

from .models import LibreAuthors


# admin.site.register(LibreAuthors)

@admin.register(LibreAuthors)
class LibreAuthorsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'time_create', 'is_published']
    list_display_links = ['id', 'title']
    list_filter = ['id', 'title', 'author', 'time_create']
    list_editable = ('is_published', )
    list_per_page = 6
    prepopulated_fields = {'slug': ('title',), }
    ordering = ['time_create', 'title']

    search_fields = ['title', 'author', 'content']
