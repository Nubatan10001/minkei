from django.shortcuts import render, get_object_or_404
from .models import MicroEconArticle
import markdown

def MicroEconArticleListView(request):
    articles = MicroEconArticle.objects.all().order_by("published_date")  # 古い順に並び替え
    return render(request, 'intro_microecon/intro_microecon_list.html', {'articles': articles})

def MicroEconArticleDetail(request, slug):
    article = get_object_or_404(MicroEconArticle, slug=slug)
    article.content = markdown.markdown(article.content)
    return render(request, 'intro_microecon/intro_microecon_detail.html', {'article': article})
