import markdown

from django.shortcuts import render, redirect

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from Blogs.models import Post, Friends, Cover

# Create your views here.

#主页视图函数，直接返回主页
def index(request):
    page = request.GET.get ('page')

    articles = Post.objects.all()
    friends = Friends.objects.all()

    paginator = Paginator(articles, 9)
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(Paginator.num_pages)

    context = {'articles': articles, 'friends': friends}
    return render(request, 'index.html', context)

def detail(request):
    article_id = request.GET.get('query')
    if article_id:
        article = Post.objects.get(id= article_id)
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
            article_pre = Post.objects.get(id=str(int(article_id) -1))
        except Exception:
            article_next = Post.objects.get (id=str (int (article_id) + 1))
            context = {'article': article, 'article_next': article_next, 'friends': friends,
                       'cover': cover}
            flag = False
        try:
            article_next = Post.objects.get(id=str(int(article_id) + 1))
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

