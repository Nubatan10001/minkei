"""
URL configuration for minkei project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),                                             # ホームページ
    path("prof/", include("prof.urls")),                                        # プロフィール
    path('beginning/', include('beginning.urls')),                              # はじめに
    path('markdownx/', include('markdownx.urls')),                              # マークダウン記法に関するURL 
    path("roadmap/", include("roadmap.urls")),                                  # 経済学のロードマップ
    path('intro-econ/', include('intro_econ.urls', namespace='intro_econ')),    # 経済学 入門（講義）
    path('intro-microecon/', include('intro_microecon.urls')),                  # ミクロ経済学 入門（講義）
    path('advanced_microecon/', include('advanced_microecon.urls')),            # ミクロ経済学 応用（講義）
    path('intro-macroecon/', include('intro_macroecon.urls')),                  # マクロ経済学 入門（講義）
    path('advanced-macroecon/', include('advanced_macroecon.urls')),            # マクロ経済学 応用（講義）
    path('intro-metrics/', include('intro_metrics.urls')),                      # 計量経済学 入門（講義）
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)