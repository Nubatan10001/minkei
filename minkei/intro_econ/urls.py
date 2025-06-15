from django.urls import path
from .views import EconArticleListView, IntroEconArticle

app_name = 'intro_econ'

urlpatterns = [
    path('', EconArticleListView, name='intro_econ_list'),
    path('<slug:slug>/', IntroEconArticle, name='intro_econ_article'),
]
