from django.contrib import admin

from .models import Listing


@admin.action(description='Опубликовать')
def make_published(self, request, queryset):
    queryset.update(is_published=True)

@admin.action(description='Снять с публикации')
def make_unpublished(self, request, queryset):
    queryset.update(is_published=False)

@admin.action(description='Открыть')
def state_up(self, request, queryset):
    queryset.update(state=True)

@admin.action(description='Закрыть')
def state_down(self, request, queryset):
    queryset.update(state=False)

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', 'email')}

    list_display = ('title', 'overview', 'date_published', 'rating', 'state')
    date_hierarchy = 'date_published'
    list_filter = ('is_published', 'rating', 'state',)
    readonly_fields = ('date_published', )
    actions = (make_published, make_unpublished, state_up, state_down)
    search_fields = ('title', 'id', 'overview')


# Register your models here.