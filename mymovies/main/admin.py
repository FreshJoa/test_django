from django.contrib import admin
from .models import Movie

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    #fields = ('name', 'description', 'year')
    list_display = ('name',  'year', 'released')
    list_filter =  ('year', 'rating')
    search_fields = ('name', 'description')

# Register your models here.
