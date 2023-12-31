from django import forms
from django.contrib import admin, messages
from ckeditor.widgets import CKEditorWidget

from .models import LibreAuthors


class BookAdminForm(forms.ModelForm):
    content = forms.CharField(label='Описание', widget=CKEditorWidget())

    class Meta:
        model = LibreAuthors
        fields = '__all__'


@admin.register(LibreAuthors)
class LibreAuthorsAdmin(admin.ModelAdmin):
    actions = ['set_published', 'set_draft']
    list_display = ['id', 'title', 'author', 'time_create', 'is_published']
    list_display_links = ['id', 'title']
    list_filter = ['id', 'title', 'author', 'time_create']
    list_editable = ('is_published',)
    list_per_page = 6
    form = BookAdminForm
    prepopulated_fields = {'slug': ('title',), }
    ordering = ['time_create', 'title']

    search_fields = ['title', 'author', 'content']

    @admin.action(description='SET PUBLISHED')
    def set_published(self, request, queryset):
        count = queryset.update(is_published=LibreAuthors.Status.PUBLISHED)
        self.message_user(request, f'Count of published items: {count}')

    @admin.action(description='SET DRAFT')
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=LibreAuthors.Status.DRAFT)
        self.message_user(request, f'Count of unpublished items: {count}', messages.WARNING)



