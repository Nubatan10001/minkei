from django.urls import path
from .views import MetricsArticleListView, IntroMetricsArticle

app_name = 'intro_metrics'

urlpatterns = [
    path('', MetricsArticleListView, name='intro_metrics_list'),
    path('<slug:slug>/', IntroMetricsArticle, name='intro_metrics_article'),
]
