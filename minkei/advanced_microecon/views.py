# advanced_microecon/views.py
from django.shortcuts import render, get_object_or_404
from .models import AdvancedMicroeconArticle
import markdown

def AdvancedMicroeconArticleListView(request):
    articles = AdvancedMicroeconArticle.objects.all().order_by("published_date")
    return render(request, 'advanced_microecon/advanced_microecon_list.html', {'articles': articles})

def AdvancedMicroeconArticleDetail(request, slug):
    article = get_object_or_404(AdvancedMicroeconArticle, slug=slug)
    article.content = markdown.markdown(article.content)
    return render(request, 'advanced_microecon/advanced_microecon_detail.html', {'article': article})
