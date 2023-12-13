from django.contrib import admin
from .models import Blog, Category
from django.utils.safestring import mark_safe
 
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active","is_home", "mesut_categories",)
    list_editable = ("is_active","is_home",)
    list_filter = ("is_active","is_home","categories",)

    def mesut_categories(self, obj):
        html = ""
        for category in obj.categories.all():
            html+="<li>" + category.name + "</li>"
        return mark_safe(html)

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)

