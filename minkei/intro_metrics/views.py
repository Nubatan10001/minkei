from minkei.article_views import render_article_detail, render_article_list
from .models import MetricsArticle

def MetricsArticleListView(request):
    return render_article_list(
        request,
        model=MetricsArticle,
        template_name='intro_metrics/intro_metrics_list.html',
    )

def IntroMetricsArticle(request, slug):
    return render_article_detail(
        request,
        model=MetricsArticle,
        slug=slug,
        template_name='intro_metrics/intro_metrics_detail.html',
    )
