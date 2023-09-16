from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import Film
from .form import ReviewForm

class FilmsView(View):
    '''Список фильмов'''
    def get(self, request):
        films = Film.objects.all()
        return render(request, 'films/film.html', {'film_list': films})

class FilmDetail(View):
    '''Представление одного фильма'''
    def get(self, request, slug):
        film = Film.objects.get(url=slug)
        return render(request, 'films/film_detail.html', {'film': film})
class AddReview(View):
    '''Добавление отзыва'''
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.film_id = pk
        return redirect('/')
