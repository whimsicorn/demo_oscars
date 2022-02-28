from django.contrib import admin
from .models import Films, Our_rating

@admin.register(Films)
class FilmAdmin (admin.ModelAdmin):
    list_display = ['title','director','country']
    list_filter = ['country']
    search_fields=['title','description']

admin.site.register(Our_rating)

