from django.urls import path
from .views import MicroEconArticleListView, MicroEconArticleDetail

app_name = 'intro_microecon'

urlpatterns = [
    path('', MicroEconArticleListView, name='intro_microecon_list'),
    path('<slug:slug>/', MicroEconArticleDetail, name='intro_microecon_article'),
]
