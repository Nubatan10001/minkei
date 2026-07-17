from minkei.article_views import render_article_detail, render_article_list
from .models import MacroAdvancedArticle

def MacroAdvancedListView(request):
    return render_article_list(
        request,
        model=MacroAdvancedArticle,
        template_name='advanced_macroecon/advanced_macroecon_list.html',
    )

def MacroAdvancedDetailView(request, slug):
    return render_article_detail(
        request,
        model=MacroAdvancedArticle,
        slug=slug,
        template_name='advanced_macroecon/advanced_macroecon_detail.html',
    )
