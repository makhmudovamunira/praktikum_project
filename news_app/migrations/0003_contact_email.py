# Generated by Django 5.2.1 on 2025-05-21 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0002_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.EmailField(default='m@gmail.com', max_length=254),
            preserve_default=False,
        ),
    ]
