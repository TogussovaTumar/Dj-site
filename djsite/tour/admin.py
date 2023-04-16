from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import*

class TourAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'photo', 'is_published')
    list_display_links = ('id', 'name')
    search_fields = ('name','content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {"slug": ("name",)}
    fields = ('name','slug','cat','content','photo','get_html_photo','is_published','time_create','time_update')
    readonly_fields = ('time_create','time_update','get_html_photo')
    save_on_top = True
    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")


    get_html_photo.short_decription = "Minioture"


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Tour, TourAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_title  = 'Administration page for Tours'
admin.site.site_header  = 'Administration page for Tours'