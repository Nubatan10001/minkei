from minkei.article_views import render_article_detail, render_article_list
from .models import MacroEconArticle

def MacroEconArticleListView(request):
    return render_article_list(
        request,
        model=MacroEconArticle,
        template_name='intro_macroecon/intro_macroecon_list.html',
    )

def IntroMacroEconArticle(request, slug):
    return render_article_detail(
        request,
        model=MacroEconArticle,
        slug=slug,
        template_name='intro_macroecon/intro_macroecon_detail.html',
    )
