from django.shortcuts import render
from django.db.models import Q

from advanced_macroecon.models import MacroAdvancedArticle
from advanced_microecon.models import AdvancedMicroeconArticle
from intro_econ.models import EconArticle
from intro_macroecon.models import MacroEconArticle
from intro_metrics.models import MetricsArticle
from intro_microecon.models import MicroEconArticle
from .models import SiteNews


COURSE_SECTIONS = [
    {
        "title": "まずはここから！",
        "description": "経済学を学ぶ順番を確認して、入門講義へ進みます。",
        "items": [
            {
                "title": "はじめに",
                "description": "このサイトの使い方と学び方の入口です。",
                "url_name": "beginning",
                "label": "Guide",
            },
            {
                "title": "経済学のロードマップ",
                "description": "学部レベルの全体像と科目のつながりを見渡します。",
                "url_name": "roadmap",
                "label": "Map",
            },
            {
                "title": "経済学入門（講義）",
                "description": "需要・供給から経済学の考え方を始めます。",
                "url_name": "intro_econ:intro_econ_list",
                "label": "Intro",
            },
        ],
    },
    {
        "title": "ミクロ経済学",
        "description": "個人・企業・市場の意思決定を学ぶコースです。",
        "items": [
            {
                "title": "ミクロ経済学 入門（講義）",
                "description": "消費者、生産者、市場均衡を順に扱います。",
                "url_name": "intro_microecon:intro_microecon_list",
                "label": "Basic",
            },
            {
                "title": "ミクロ経済学 応用（講義）",
                "description": "ゲーム理論や市場の失敗などへ広げます。",
                "url_name": "advanced_microecon:advanced_microecon_list",
                "label": "Advanced",
            },
        ],
    },
    {
        "title": "マクロ経済学",
        "description": "GDP、物価、雇用、政策を国全体の視点で学びます。",
        "items": [
            {
                "title": "マクロ経済学 入門（講義）",
                "description": "国民所得、金融、財政政策の基礎を扱います。",
                "url_name": "intro_macroecon:intro_macroecon_list",
                "label": "Basic",
            },
            {
                "title": "マクロ経済学 応用（講義）",
                "description": "成長理論や景気循環などへ進みます。",
                "url_name": "advanced_macroecon:advanced_macroecon_list",
                "label": "Advanced",
            },
        ],
    },
    {
        "title": "計量経済学",
        "description": "データから経済現象を読み解くための道具を学びます。",
        "items": [
            {
                "title": "計量経済学 入門（講義）",
                "description": "回帰分析と推定・検定の基礎から始めます。",
                "url_name": "intro_metrics:intro_metrics_list",
                "label": "Basic",
            },
            {
                "title": "計量経済学 応用（講義）",
                "description": "パネルデータや因果推論などを扱う予定です。",
                "label": "Soon",
                "is_pending": True,
            },
        ],
    },
    {
        "title": "これから広げる分野",
        "description": "経済史、応用分野、試験対策などを追加していく領域です。",
        "items": [
            {
                "title": "経済史 入門（講義）",
                "description": "歴史の流れから経済を捉える講義を準備中です。",
                "label": "Soon",
                "is_pending": True,
            },
            {
                "title": "各応用分野について",
                "description": "公共・労働・金融などの応用分野を整理予定です。",
                "label": "Soon",
                "is_pending": True,
            },
            {
                "title": "大学で経済学を学ぶ",
                "description": "履修や自習のコツをまとめる予定です。",
                "label": "Soon",
                "is_pending": True,
            },
        ],
    },
]

SEARCH_TARGETS = [
    ("経済学入門", EconArticle, "intro_econ:intro_econ_article"),
    ("ミクロ経済学 入門", MicroEconArticle, "intro_microecon:intro_microecon_article"),
    ("ミクロ経済学 応用", AdvancedMicroeconArticle, "advanced_microecon:advanced_microecon_article"),
    ("マクロ経済学 入門", MacroEconArticle, "intro_macroecon:intro_macroecon_article"),
    ("マクロ経済学 応用", MacroAdvancedArticle, "advanced_macroecon:advanced_macroecon_article"),
    ("計量経済学 入門", MetricsArticle, "intro_metrics:intro_metrics_article"),
]


def home(request):
    news_items = SiteNews.objects.filter(is_published=True)[:5]
    return render(
        request,
        'home/home.html',
        {
            "course_sections": COURSE_SECTIONS,
            "news_items": news_items,
        },
    )


def search(request):
    query = request.GET.get("q", "").strip()
    results = []

    if query:
        for category, model, url_name in SEARCH_TARGETS:
            articles = (
                model.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
                .order_by("published_date")
                .only("title", "slug", "published_date")
            )
            for article in articles:
                results.append(
                    {
                        "category": category,
                        "title": article.title,
                        "slug": article.slug,
                        "published_date": article.published_date,
                        "url_name": url_name,
                    }
                )

    return render(
        request,
        "home/search_results.html",
        {
            "query": query,
            "results": results,
        },
    )
