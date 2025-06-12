from .models import News

def latest_news(request):
    latest_new=News.published.all().order_by('-publish_time')[:10]

    context={
        'latest_new':latest_new
    }
    return context