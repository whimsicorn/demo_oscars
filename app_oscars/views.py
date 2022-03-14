from django.shortcuts import render, get_object_or_404, redirect
from app_oscars.models import Films, Our_rating
from django.contrib.auth import get_user_model
from f import Film

def ranking(request):
    films = Films.objects.all()
    User = get_user_model()
    users = User.objects.all()
    return render(request, 'ranking.html',{'films':films,
                                           'users':users})

def new_film(request):
    form = FilmsForm (request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect(ranking)

    return render(request, 'film_form.html', {'form':form})

def edit_film(request, id):
    film = get_object_or_404(Films, pk=id)
    form = FilmsForm (request.POST or None, request.FILES or None,
                      instance=film)

    if form.is_valid():
        form.save()
        return redirect(ranking)

    return render(request, 'film_form.html', {'form':form})

def delete_film(request, id):
    film = get_object_or_404(Films, pk=id)

    if request.method == "POST":
        film.delete()
        return redirect(ranking)

    return render(request, 'confirm.html', {'film':film})

def films_rating(request, id):
    rating = Our_rating.objects.all()
    films = get_object_or_404(Films, pk=id)
    return render(request, 'films_rating.html', {'ratig':rating, 'films':films,})


