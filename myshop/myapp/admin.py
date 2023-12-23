from django.contrib import admin

from .models import Product



admin.site.site_header = 'Onimum Admin Portal'
admin.site.site_title = 'Title of Onimum Admin Portal'
admin.site.index_title = "Welcome to Onimum Admin"


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'image')
    search_fields = ('name', 'price', 'description')
    list_editable = ('price', 'description')
    actions = ('make_zero',)

    def make_zero(self, request, queryset):
        queryset.update(price=0)


admin.site.register(Product, ProductAdmin)