from django.contrib import admin
from .models import Film, Genre, Direction, Reviews

admin.site.register(Film)
admin.site.register(Genre)
admin.site.register(Direction)
admin.site.register(Reviews)
