from django.contrib.auth.models import User
from django.db.models import CASCADE
from django.urls import reverse
from django.utils import timezone

from django.db import models

# Create your models here.

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=News.Status.Published)

class Category(models.Model):
    name=models.CharField(max_length=150)

    def __str__(self):
        return self.name

class News(models.Model):

    class Status(models.TextChoices):
        Draft='DF', 'Draft'
        Published='PB', 'Published'

    title=models.CharField(max_length=250)
    slug=models.SlugField(max_length=250)
    body=models.TextField()
    image=models.ImageField(upload_to='news/images')
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    publish_time=models.DateTimeField(default=timezone.now)
    created_time=models.DateTimeField(auto_now_add=True)
    updated_time=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=2,
                            choices=Status.choices,
                            default=Status.Draft
                            )

    view_count = models.PositiveIntegerField(default=0)  # Yangi qo'shilgan ustun

    objects=models.Manager() # default manager
    published=PublishedManager()
    class Meta:
        ordering=['-publish_time']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news_detail_page', args=[self.slug])

class Contact(models.Model):
    message=models.CharField(max_length=1000)
    name=models.CharField(max_length=50)
    email=models.EmailField()
    subject=models.CharField(max_length=300)

    def __str__(self):
        return self.email   # 993107070

class Comment(models.Model):
    news=models.ForeignKey(News, on_delete=models.CASCADE, related_name='comments')
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    body=models.TextField()
    created_time=models.DateTimeField(auto_now_add=True)
    activate=models.BooleanField(default=True)

    class Meta:
        ordering=['created_time']

    def __str__(self):
        return f"Comment - {self.body} by {self.user}"
