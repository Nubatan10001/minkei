from django.shortcuts import get_object_or_404, render


def render_article_list(request, *, model, template_name):
    articles = model.objects.all().order_by("published_date")
    return render(request, template_name, {"articles": articles})


def render_article_detail(request, *, model, slug, template_name):
    article = get_object_or_404(model, slug=slug)
    content_html = article.formatted_markdown()
    return render(
        request,
        template_name,
        {
            "article": article,
            "content_html": content_html,
        },
    )
