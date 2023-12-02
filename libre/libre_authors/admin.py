from django.contrib import admin

from .models import LibreAuthors

# admin.site.register(LibreAuthors)
@admin.register(LibreAuthors)
class LibreAuthorsAdmin(admin.ModelAdmin):
	list_display = ['title', 'author', 'time_create', 'time_update']
	list_filter = ['title', 'author', 'time_create']

	search_fields = ['title', 'content']

