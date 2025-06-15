# intro_macroecon/urls.py
from django.urls import path
from .views import MacroEconArticleListView, IntroMacroEconArticle

app_name = 'intro_macroecon'

urlpatterns = [
    path('', MacroEconArticleListView, name='intro_macroecon_list'),
    path('<slug:slug>/', IntroMacroEconArticle, name='intro_macroecon_article'),
]
