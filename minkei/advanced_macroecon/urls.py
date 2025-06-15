from django.urls import path
from .views import MacroAdvancedListView, MacroAdvancedDetailView

app_name = 'advanced_macroecon'

urlpatterns = [
    path('', MacroAdvancedListView, name='advanced_macroecon_list'),
    path('<slug:slug>/', MacroAdvancedDetailView, name='advanced_macroecon_article'),
]
