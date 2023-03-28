from django.contrib import admin

from .models import Movie

@admin.register(Movie)
class AuthorAdmin(admin.ModelAdmin):
    pass
