from django.contrib import admin
from .models import Genre, Movie, Movie_Comment

# Register your models here.
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(Movie_Comment)