from django.shortcuts import render
from .models import RoadmapPage
from markdownx.utils import markdownify

def roadmap_view(request):
    page = RoadmapPage.objects.first()  # 1つのページのみ表示
    content_html = markdownify(page.content) if page else ""  # Markdown を HTML に変換
    return render(request, "roadmap/roadmap.html", {"page": page, "content_html": content_html})
