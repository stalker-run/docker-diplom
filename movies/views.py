from django.shortcuts import redirect, render
from django.core.files.storage import FileSystemStorage

from .models import Movie
from .forms import MovieForm


def add(request):
    if request.method == 'GET':
        return render(request, 'add-form.html', context={'form': MovieForm()})

    if request.method == "POST" and request.FILES:
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    return redirect('index')


def add(request):
    if request.method == 'GET':
        return render(request, 'add-form.html', context={'form': MovieForm()})

    if request.method == "POST" and request.FILES:
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    return redirect('index')


def index(request):
    movies = Movie.objects.all()
    print(movies)
    return render(request, 'index.html', context={'movies': movies})
