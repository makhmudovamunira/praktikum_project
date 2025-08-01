# Generated by Django 5.2.1 on 2025-07-22 18:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0004_news_view_count'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='news_app.news')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentd', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_time'],
            },
        ),
    ]
