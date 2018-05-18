# _*_encoding:utf-8 _*_
import datetime

from django.db import models

from django.contrib.auth.models import User

from django.urls import reverse
# Create your models here.

# 解决字符编码问题
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


# 分类部分
class Category(models.Model):
    name = models.CharField(verbose_name="分类" ,max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "分类"
        verbose_name_plural = "分类"


# 标签部分
class Tag(models.Model):
    name = models.CharField(verbose_name="标签", max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = "标签"


# 文章的题图部分
class Cover(models.Model):
    word = models.CharField(verbose_name="字母", max_length=10, null= False, unique= True)
    cover = models.URLField(verbose_name="链接地址", null=False)
    english = models.CharField(verbose_name="英语", max_length=100, null=False)
    chinese = models.CharField(verbose_name="中文", max_length=100, null=False)


    def __str__(self):
        return self.cover


    class Meta:
        verbose_name = "题图"
        verbose_name_plural = "题图"

# 替换自带的objects管理器，自己可以来编写自己想实现的部分。
class PostManager(models.Manager):
    def distinct_date(self):
        date_list = []
        dates = self.values('created_time')

        for date in dates:
            date = date['created_time'].strftime('%Y/%m')
            if date not in date_list:
                date_list.append(date)

        return date_list

# 正文部分
class Post(models.Model):
    title = models.CharField(verbose_name="标题" ,max_length=150, blank= False, null= False, unique=True)
    cover = models.ForeignKey(to= Cover, verbose_name="题图")
    content = models.TextField(verbose_name="正文", blank= True, null= True)
    created_time = models.DateTimeField(verbose_name="创建时间")
    modified_time = models.DateTimeField(verbose_name="修改时间")
    views = models.PositiveIntegerField(verbose_name="阅读量", default= '0')
    category = models.ForeignKey(to= Category, verbose_name="分类")
    tag = models.ManyToManyField(to= Tag, verbose_name="标签")
    author = models.ForeignKey(to=User, verbose_name='作者', default= "SKYNE" )
    # 当使用管理器时会替换掉默认的objects，因此，需要调整views中的视图部分
    object = PostManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('Blogs:index', kwargs={'pk', self.pk})

    class Meta:
        ordering = ['-created_time']
        verbose_name = "文章"
        verbose_name_plural = "文章"

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

class Friends(models.Model):
    name  = models.CharField(verbose_name= "名称", max_length=50, null=False, blank=False)

    url = models.URLField(verbose_name="链接",null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "友情链接"
        verbose_name_plural = "友情链接"
