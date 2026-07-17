from minkei.article_views import render_article_detail, render_article_list
from .models import AdvancedMicroeconArticle

def AdvancedMicroeconArticleListView(request):
    return render_article_list(
        request,
        model=AdvancedMicroeconArticle,
        template_name='advanced_microecon/advanced_microecon_list.html',
    )

def AdvancedMicroeconArticleDetail(request, slug):
    return render_article_detail(
        request,
        model=AdvancedMicroeconArticle,
        slug=slug,
        template_name='advanced_microecon/advanced_microecon_detail.html',
    )
