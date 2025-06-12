from django.contrib import admin
from .models import News, Category, Contact

# Register your models here.
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'publish_time', 'status','view_count']
    list_filter = ['status', 'created_time', 'publish_time']
    prepopulated_fields = {'slug':('title',)} #slug maydoni title ga qarab avtomatik to‘ldiriladi.
    date_hierarchy = 'publish_time' #admin panelda publish_time ustuniga qarab sanaga asoslangan filtrlash menyusi
    search_fields = ['title', 'body'] # admin panelda title va body maydonlari bo‘yicha qidiruv
    ordering = ['status', 'publish_time']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


admin.site.register(Contact)