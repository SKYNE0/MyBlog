from django.contrib import admin
from Blogs.models import Tag, Category, Post, Friends, Cover
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'cover','created_time', 'modified_time', 'category', 'author']

admin.site.register(Post)

admin.site.register(Category)

admin.site.register(Tag)

admin.site.register(Friends)

admin.site.register(Cover)

