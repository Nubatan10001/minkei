from django.shortcuts import render
from .models import BeginningPage

def beginning_page(request):
    page = BeginningPage.objects.first()  # 1つだけデータを取得
    return render(request, "beginning/beginning.html", {"page": page, "content_html": page.formatted_markdown() if page else ""})
