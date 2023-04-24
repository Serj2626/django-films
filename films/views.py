from django.shortcuts import render
from django.views.generic.base import View
from .models import Film


class FilmsView(View):
    '''Список фильмов'''

    def get(self, request):
        films = Film.objects.all()
        return render(request, 'films/film.html', {'films_list': films})
