from minkei.article_views import render_article_detail, render_article_list
from .models import MicroEconArticle

def MicroEconArticleListView(request):
    return render_article_list(
        request,
        model=MicroEconArticle,
        template_name='intro_microecon/intro_microecon_list.html',
    )

def MicroEconArticleDetail(request, slug):
    return render_article_detail(
        request,
        model=MicroEconArticle,
        slug=slug,
        template_name='intro_microecon/intro_microecon_detail.html',
    )
