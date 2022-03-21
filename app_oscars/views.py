from django.shortcuts import render, get_object_or_404, redirect
from app_oscars.models import Films, Review
from django.contrib.auth import get_user_model
from .forms import FilmsForm
from django.contrib.auth.decorators import login_required

def ranking(request):
    films = Films.objects.all()
    User = get_user_model()
    users = User.objects.all()
    reviews = Review.objects.all()
    return render(request, 'ranking.html',{'films':films,
                                           'users':users,
                                           'reviews':reviews})
@login_required
def new_film(request):
    form = FilmsForm (request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect(ranking)

    return render(request, 'film_form.html', {'form':form})

@login_required
def edit_film(request, id):
    film = get_object_or_404(Films, pk=id)
    form = FilmsForm (request.POST or None, request.FILES or None,
                      instance=film)

    if form.is_valid():
        form.save()
        return redirect(ranking)

    return render(request, 'film_form.html', {'form':form})

@login_required
def delete_film(request, id):
    films = get_object_or_404(Films, pk=id)

    if request.method == "POST":
        films.delete()
        return redirect(ranking)

    return render(request, 'confirm.html', {'films':films})


def films_rating(request, id):
    films = get_object_or_404(Films, pk=id)
    User = get_user_model()
    users = User.objects.all()
    return render(request, 'films_rating.html', {'films':films,
                                                 'users':users})


