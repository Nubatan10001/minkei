from minkei.article_views import render_article_detail, render_article_list
from .models import EconArticle

def EconArticleListView(request):
    return render_article_list(
        request,
        model=EconArticle,
        template_name='intro_econ/intro_econ_list.html',
    )

def IntroEconArticle(request, slug):
    return render_article_detail(
        request,
        model=EconArticle,
        slug=slug,
        template_name='intro_econ/intro_econ_detail.html',
    )
