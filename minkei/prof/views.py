from django.views.generic import TemplateView


class ProfListView(TemplateView):
    template_name = "prof/prof.html"
