from django.urls import path
from .views import roadmap_view

urlpatterns = [
    path("", roadmap_view, name="roadmap"),
]
