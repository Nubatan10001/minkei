from django.shortcuts import render, get_object_or_404
from .models import MacroAdvancedArticle
import markdown

def MacroAdvancedListView(request):
    articles = MacroAdvancedArticle.objects.all().order_by("published_date")  # 古い順
    return render(request, 'advanced_macroecon/advanced_macroecon_list.html', {'articles': articles})

def MacroAdvancedDetailView(request, slug):
    article = get_object_or_404(MacroAdvancedArticle, slug=slug)
    article.content = markdown.markdown(article.content)
    return render(request, 'advanced_macroecon/advanced_macroecon_detail.html', {'article': article})
