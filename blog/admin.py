from django.contrib import admin
from . import models


class FilterByTitle(admin.SimpleListFilter):
    title = " کلید های پر تکرار"
    parameter_name = "title"

    def lookups(self, request, model_admin):
        return (
            ("django", "جنگو"),
            ("html", "اچ دی ام ال"),
            ("sql", "اس کیو ال"),
        )

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(title__icontains=self.value())


class CommentInLine(admin.TabularInline):
    model = models.Comment


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("__str__", "author", "published", "show_img")
    list_filter = ("published", FilterByTitle)
    inlines = (CommentInLine,)


admin.site.register(models.Category)
admin.site.register(models.Comment)
admin.site.register(models.Message)
admin.site.register(models.Like)
