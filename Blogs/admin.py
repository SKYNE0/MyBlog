#_*_encoding:utf-8 _*_
from django.contrib import admin
from .models import Tag, Category, Post, Friends, Cover
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'cover','created_time', 'modified_time', 'category', 'author']


admin.site.site_header = "喵喵，主人您来啦， ヽ(✿ﾟ▽ﾟ)ノ"
admin.site.site_title = "欢迎来到SKYNE管理界面"
admin.site.register(Post)

admin.site.register(Category)

admin.site.register(Tag)

admin.site.register(Friends)

admin.site.register(Cover)

