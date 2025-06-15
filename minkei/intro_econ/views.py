from django.shortcuts import render, get_object_or_404
from .models import EconArticle
import markdown

def EconArticleListView(request):
    articles = EconArticle.objects.all().order_by("published_date")  # 古い順に並び替え
    return render(request, 'intro_econ/intro_econ_list.html', {'articles': articles})

def IntroEconArticle(request, slug):
    article = get_object_or_404(EconArticle, slug=slug)
    article.content = markdown.markdown(article.content)
    return render(request, 'intro_econ/intro_econ_detail.html', {'article': article})
