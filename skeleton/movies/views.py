from django.shortcuts import render, redirect, get_list_or_404
from django.views.decorators.http import require_safe
from .models import Movie, Genre
from community.models import Review
from django.db.models import Q
from django.http import JsonResponse


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
    
    context = {
        'genre_lst' : Genre.objects.all()
    }
    return render(request, 'movies/recommended.html', context)


# new 
@require_safe
def recommend(request):
    my = request.GET
    # print(my.getlist('lst[]'))
    lst = my.getlist('lst[]')
    lst = list(map(int, lst))
    # print(lst)
    # 평점순 정렬 리스트
    vote_lst = []

    movie_join = Movie.objects.prefetch_related('genres')
    for i in movie_join:
        flag = False
        for j in i.genres.all():
            if j.id in lst:
                flag = True
        if flag == True:
            vote_lst.append((i.poster_path, i.vote_average))
    vote_lst.sort(key=lambda x:-x[1])
    # print(vote_lst)
    
    context = {
        'data': vote_lst[:10]
    }
    return JsonResponse(context, safe=False)



