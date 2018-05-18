# -*- coding: UTF-8 -*- 

import markdown

from django.shortcuts import render, redirect

from django.views.generic import View, ListView

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from Blogs.models import Post, Friends, Cover, Tag, Category

# Create your views here.

"""
简单使用基于类的视图代替基于函数的视图，还正在学习基于类的视图。

下面Post.object的部分，并没有写错。因为在models部分，替换了原本的objects的管理器。
"""


#主页视图函数，直接返回主页
class Index(View):

    def get(self, request):
        page = request.GET.get ('page')

        articles = Post.object.all()

        friends = Friends.objects.all()

        paginator = Paginator(articles, 9)
        try:
            articles = paginator.page(page)
        except PageNotAnInteger:
            articles = paginator.page(1)
        except EmptyPage:
            articles = paginator.page(Paginator.num_pages)

        context = {'articles': articles, 'friends': friends, 'headlines':'The latest Article'}
        return render(request, 'index.html', context)


def detail(request):
    article_id = request.GET.get('query')
    if article_id:
        article = Post.object.get(id= article_id)
        cover = Cover.objects.get(id= article.cover_id)
        article.content = markdown.markdown(article.content,
                                      extensions=['markdown.extensions.fenced_code',
                                         'markdown.extensions.extra',
                                         'markdown.extensions.codehilite',
                                         'markdown.extensions.toc',
                                      ])

        friends = Friends.objects.all()

        # 下面的是判断一篇文章是否有前一篇或者后一篇
        flag = True
        try:
            if article_id == '35':
                article_pre = Post.object.get(id=str(int(article_id) - 2))
            else:
                article_pre=Post.object.get(id=str(int(article_id) - 1))
        except Exception:
            article_next = Post.object.get (id=str (int (article_id) + 1))
            context = {'article': article, 'article_next': article_next, 'friends': friends,
                       'cover': cover}
            flag = False
        try:
            article_next = Post.object.get(id=str(int(article_id) + 1))
        except Exception:
            context = {'article': article, 'article_pre': article_pre, 'friends': friends,
                       'cover': cover}
            flag = False


        if flag:
            context = {'article': article,
                   'article_pre': article_pre,
                   'article_next': article_next,
                   'friends': friends,
                   'cover': cover}

        return render(request, 'detail.html', context)

    return redirect(to= 'index')


def archive(request, year, month):
    posts = Post.object.filter(created_time__year=year,
                               created_time__month=month,
                               ).order_by('-created_time')

    friends = Friends.objects.all()

    context = {'articles': posts, 'friends': friends, 'headlines':'According To Month Classification'}
    return render(request, 'category.html', context)

class Label(ListView):
    template_name = 'category.html'
    context_object_name = 'articles'

    def get_queryset(self):
        articles = Post.object.filter(tag=self.kwargs['tag_id'])
        return articles

    def get_context_data(self, **kwargs):
        kwargs['headlines'] = 'According To Label Classification'
        return super(Label, self).get_context_data(**kwargs)

class Categorys(ListView):
    template_name = 'category.html'
    context_object_name = 'articles'

    def get_queryset(self):
        articles = Post.object.filter(category=self.kwargs['category_id'])
        return articles

    def get_context_data(self, **kwargs):
        kwargs['headlines'] = 'Categorization By Category'
        return super(Categorys, self).get_context_data(**kwargs)


class Archives(ListView):
    template_name = 'archives.html'
    context_object_name = 'context'

    def get_queryset(self):
        pass

    def get_context_data(self, **kwargs):
        kwargs['archives'] = Post.object.distinct_date()
        kwargs['labels'] = Tag.objects.all()
        kwargs['categorys'] = Category.objects.all()
        kwargs['friends'] = Friends.objects.all()
        kwargs['headlines'] = 'According To Time'

        return super(Archives, self).get_context_data(**kwargs)
