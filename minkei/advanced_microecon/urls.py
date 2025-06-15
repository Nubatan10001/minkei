# advanced_microecon/urls.py
from django.urls import path
from .views import AdvancedMicroeconArticleListView, AdvancedMicroeconArticleDetail

app_name = 'advanced_microecon'

urlpatterns = [
    path('', AdvancedMicroeconArticleListView, name='advanced_microecon_list'),
    path('<slug:slug>/', AdvancedMicroeconArticleDetail, name='advanced_microecon_article'),
]
