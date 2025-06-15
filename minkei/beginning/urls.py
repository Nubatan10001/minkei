from django.urls import path
from .views import beginning_page

urlpatterns = [
    path("", beginning_page, name="beginning"),
]
