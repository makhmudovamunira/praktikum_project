from datetime import timedelta
import random

from django.db.models import F
from django.urls import reverse_lazy
from django.utils import timezone

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DeleteView, UpdateView
from .forms import ContactForm

from .models import News, Category

# Create your views here.

def news_list(request):
    news_list=News.published.all()
    # news_list=News.objects.filter(status=News.Status.Published)
    # news_list=News.objects.all()
    context={
        'news_list':news_list
    }

    return render(request, 'news/news_list.html', context=context)

def news_detail(request, news):
    news=get_object_or_404(News, slug=news,status=News.Status.Published)

    News.objects.filter(pk=news.pk).update(view_count=F('view_count')+1)
    news.refresh_from_db()
    context={
        'news':news
    }
    return render(request, 'news/news_detail.html', context=context)

def homepageView(request):
    news_list = News.published.all().order_by('-publish_time')[:8]
    categories=Category.objects.all()

    one_week_ago=timezone.now()-timedelta(days=15)
    weekly_news=News.published.filter(publish_time__gte=one_week_ago).order_by('-publish_time')[:6]

    # Oxirgi 15 ta yangilikni olamiz
    latest_news = News.objects.filter(status='PB').order_by('-publish_time')[:15]

    # Tasodifiy 4 tasini tanlaymiz
    random_news = random.sample(list(latest_news), min(4, len(latest_news)))

    # Bir hafta ichida eng ko'p ko'rilgan 10 ta yangilik
    top_news = News.objects.filter(
        publish_time__gte=one_week_ago,
        status=News.Status.Published
    ).order_by('-view_count')[:8]

    context={
        'news_list':news_list,
        'categories':categories,
        'weekly_news':weekly_news,
        'random_news':random_news,
        'top_news':top_news,
    }

    return render(request, 'news/home.html', context)



class ContactPageView(TemplateView):
    template_name = 'news/home.html'

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context={
            'form':form
        }
        return render(request,'news/home.html', context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if request.method=="POST" and form.is_valid():
            form.save()
            return HttpResponse("<h2>Biz bilan bog'langaningiz uchun tashakkur</h2>")

        context={
            'form':form
        }

        return render(request,'news/home.html', context)

class ViewCategory(TemplateView):
    template_name = 'news/categori.html'



class UzNewsView(ListView):
    model = News
    template_name = 'news/uzbek.html'
    context_object_name = 'uzbek_news'

    def get_queryset(self):
        return self.model.published.all().filter(category__name='Uzbekistan')


class ForeignNewsView(ListView):
    model = News
    template_name = 'news/foreign.html'
    context_object_name = 'foreign_news'
    def get_queryset(self):
        return self.model.published.all().filter(category__name='Jahon')


class SportNewsView(ListView):
    model = News
    template_name = 'news/sport.html'
    context_object_name = 'sport_news'
    def get_queryset(self):
        return  self.model.published.all().filter(category__name='Sport')


class TexnologyNewsView(ListView):
    model = News
    template_name = 'news/texnology.html'
    context_object_name = 'texnology_news'
    def get_queryset(self):
        return self.model.published.all().filter(category__name='Fan')


class NewsUpdateView(UpdateView):
    model = News
    fields = ['title', 'body', 'image', 'category', 'status']
    template_name = 'crud/news_edit.html'

class NewsDeleteView(DeleteView):
    model = News
    template_name = 'crud/news_delete.html'
    success_url = reverse_lazy('home_page')

