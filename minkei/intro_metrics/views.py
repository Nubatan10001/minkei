from django.shortcuts import render, get_object_or_404
from .models import MetricsArticle
import markdown

def MetricsArticleListView(request):
    articles = MetricsArticle.objects.all().order_by("published_date")  # 古い順に表示
    return render(request, 'intro_metrics/intro_metrics_list.html', {'articles': articles})

def IntroMetricsArticle(request, slug):
    article = get_object_or_404(MetricsArticle, slug=slug)
    article.content = markdown.markdown(article.content)
    return render(request, 'intro_metrics/intro_metrics_detail.html', {'article': article})

