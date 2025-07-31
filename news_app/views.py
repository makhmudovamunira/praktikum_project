from datetime import timedelta
import random

from hitcount.utils import get_hitcount_model
from hitcount.views import HitCountDetailView, HitCountMixin

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import F, Q
from django.template.defaultfilters import title
from django.urls import reverse_lazy
from django.utils import timezone

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils.text import slugify
from django.utils.translation.trans_real import activate
from django.views.generic import TemplateView, ListView, DeleteView, UpdateView, CreateView
from .forms import ContactForm, CommentForm
from config.custom_permissions import OnlyLoggedSuperUser
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


def news_detail(request, news, context=None):
    news=get_object_or_404(News, slug=news,status=News.Status.Published)
    # hit orqali ko'rishlar sonini aniqlash
    hit_count = get_hitcount_model().objects.get_for_object(news)
    hits = hit_count.hits
    context={}
    hitcontext = context['hit_count'] = {'pk': hit_count.pk}
    hit_count_response = HitCountMixin.hit_count(request, hit_count)
    if hit_count_response.hit_counted:
        hits = hits + 1
        hitcontext['hit_counted'] = hit_count_response.hit_counted
        hitcontext['hit_message'] = hit_count_response.hit_message
        hitcontext['total_hits'] = hits



    comment=news.comments.filter(activate=True)
    comment_count=comment.count()
    new_comment=None
    if request.method=='POST':
        comment_form=CommentForm(data=request.POST)
        if comment_form.is_valid():
            #yangi comment obyetkini yaratamzi lekin db ga saqlamaymiz
            new_comment = comment_form.save(commit=False)
            new_comment.news=news
            #commentariya egasini tanladik
            new_comment.user=request.user
            #malumotlar bazasiga saqlaymiz
            new_comment.save()
            comment_form=CommentForm()

    else:
        comment_form=CommentForm

    News.objects.filter(pk=news.pk).update(view_count=F('view_count')+1)
    news.refresh_from_db()
    context={
        'news':news,
        'comments':comment,
        'new_comment':new_comment,
        'comment_form':comment_form,
        'comment_count':comment_count,
    }
    return render(request, 'news/news_detail.html', context=context)

def homepageView(request):
    news_list = News.published.all().order_by('-publish_time')[:8]
    categories=Category.objects.all()

    one_week_ago=timezone.now()-timedelta(days=1000)
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


class NewsUpdateView(OnlyLoggedSuperUser ,UpdateView):
    model = News
    fields = ['title', 'body', 'image', 'category', 'status']
    template_name = 'crud/news_edit.html'

class NewsDeleteView(OnlyLoggedSuperUser ,DeleteView):
    model = News
    template_name = 'crud/news_delete.html'
    success_url = reverse_lazy('home_page')


class NewCreateView(OnlyLoggedSuperUser ,CreateView):
    model = News
    template_name = 'crud/news_create.html'
    fields = ('title', 'slug', 'body', 'image', 'category', 'status')
    success_url =reverse_lazy('home_page')

    def form_valid(self, form):
        # Agar slug kiritilmagan bo'lsa, avtomatik yaratamiz
        if not form.instance.slug:
            form.instance.slug = slugify(form.instance.title)  # title field asosida
        return super().form_valid(form)


class SearchResultView(ListView):
    model = News
    template_name = 'news/search_result.html'
    context_object_name = 'all_news'


    def get_queryset(self):
        query=self.request.GET.get('q')
        return News.objects.filter(
            Q(title__icontains=query) | Q(body__icontains=query)
        )
