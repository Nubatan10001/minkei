from django.views.generic import ListView
from .models import Prof
from .forms import ProfForm

class ProfListView(ListView):
    model = Prof
    template_name = "prof/prof.html"
    context_object_name = "profs"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = ProfForm()
        return context
