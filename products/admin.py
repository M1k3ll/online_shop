from django.contrib import admin
from .models import Product, Comment


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'active', ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['product', 'author', 'body', 'stars', 'active', ]


class CommentInline(admin.TabularInline):
    model = Comment
    fields = ['product', 'author', 'body', 'stars', 'active', ]
    # extra = 1

# class CommentInline(admin.StackedInline):
#     model = Comment
#     fields = ['product', 'author', 'body', 'stars', 'active', ]
