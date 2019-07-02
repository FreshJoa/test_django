from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie
from .forms import MovieForm
from django.contrib.auth.decorators import login_required


def movies_list(request):
    filmy= Movie.objects.all()
    return render(request, 'list_of_movies.html', {'filmy': filmy})

@login_required
def new_movie(request):
    form = MovieForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect(movies_list)


    return render(request, 'form_movie.html', {'form': form})

@login_required
def edit_movie(request, id):
    film = get_object_or_404(Movie, pk = id)
    #jezeli film istnieje to form zostanie wypełniony danymi z bazy danych
    form = MovieForm(request.POST or None, request.FILES or None, instance=film)

    if form.is_valid():
        form.save()
        return redirect(movies_list)

    return render(request, 'form_movie.html', {'form': form})

@login_required
def delete_movie(request, id):
    film = get_object_or_404(Movie, pk=id)

    if request.method == 'POST':
        film.delete()
        return redirect(movies_list)

    return render(request, 'confirm.html', {'film':film})


# Create your views here.
