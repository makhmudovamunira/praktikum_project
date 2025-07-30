from django.contrib import admin
from django.utils.timezone import activate

from .models import News, Category, Contact, Comment

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


#2-usul
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'body', 'created_time', 'activate']
    list_filter = ['activate', 'body']
    search_fields = ['user', 'body']
    actions=['disabled_comments', 'activate_comments']

    def disable_comments(self, request, queryset):
        queryset.update(activate=False)

    def activate_comments(self, request, queryset):
        queryset.update(activate=True)

#1-usul
#admin.site.register(Comment, CommentAdmin)