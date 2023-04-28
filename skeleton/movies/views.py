from django.shortcuts import render, redirect, get_list_or_404
from django.views.decorators.http import require_safe
from .models import Movie, Genre
from community.models import Review
from django.db.models import Q


# Create your views here.
@require_safe
def index(request):
    movie_lst = Movie.objects.all()
    # print(movie_lst)
    context = {
        'movie_lst':movie_lst,
    }
    return render(request, 'movies/index.html', context)
    pass


@require_safe
def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    context = {
        'movie': movie,
        'genre_lst': movie.genres.all()
    }
    return render(request, 'movies/detail.html', context)


@require_safe
def recommended(request):
    lst = []

    # q = Q()
    # for i in range(len(lst)):
    #     q.add(pk = i)
    


    # genre = Genre.objects.get(pk=12) | Genre.objects.get(pk=14)
    genre = Genre.objects.filter(Q(pk=12)|Q(pk=14))
    print(genre)
    print(genre.all())


    context = {
        'genre_lst' : Genre.objects.all()
    }
    return render(request, 'movies/recommended.html', context)



