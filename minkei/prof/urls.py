from django.urls import path
from .views import ProfListView 

urlpatterns = [
    path("", ProfListView.as_view(), name="prof"), 
]