from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'pub_date'
    list_display = (
        'id',
        'title',
        'posted_by',
        'is_published',
        'pub_date',
        'votes'
    )
    list_display_links = ('id', 'title')
    list_editable = ('is_published',)
    list_filter = ('posted_by',)
    list_per_page = 25


admin.site.register(Post, PostAdmin)