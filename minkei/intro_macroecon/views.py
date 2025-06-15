# intro_macroecon/views.py
from django.shortcuts import render, get_object_or_404
from .models import MacroEconArticle
import markdown

def MacroEconArticleListView(request):
    articles = MacroEconArticle.objects.all().order_by("published_date")
    return render(request, 'intro_macroecon/intro_macroecon_list.html', {'articles': articles})

def IntroMacroEconArticle(request, slug):
    article = get_object_or_404(MacroEconArticle, slug=slug)
    article.content = markdown.markdown(article.content)
    return render(request, 'intro_macroecon/intro_macroecon_detail.html', {'article': article})
