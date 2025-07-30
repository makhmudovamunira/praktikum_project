from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

from .views import news_list, news_detail, homepageView, ContactPageView,ViewCategory,\
    UzNewsView, ForeignNewsView, TexnologyNewsView, SportNewsView, NewsUpdateView,NewsDeleteView, NewCreateView, SearchResultView

urlpatterns=[
    path('category', ViewCategory.as_view(), name='category_page'),
    path('', homepageView, name='home_page'),
    path('news/create', NewCreateView.as_view(), name='new_create'),
    path('news/<slug:news>/', news_detail, name='news_detail_page'),
    path('news/<slug>/edit/', NewsUpdateView.as_view(), name='news_update'),
    path('news/<slug>/delete/', NewsDeleteView.as_view(), name='news_delete'),
    path('news/', news_list, name='all_news_list'),
    path('contact-us/', ContactPageView.as_view(), name='contact_page'),
    path('uzbek-news/', UzNewsView.as_view(), name='uz_news_page'),
    path('foreign-news/', ForeignNewsView.as_view(), name='foreign_news_page'),
    path('sport-news/', SportNewsView.as_view(), name='sport_news_page'),
    path('fan-news/', TexnologyNewsView.as_view(), name='fan_news_page'),
    path('searchresult/', SearchResultView.as_view(), name='search_result'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


