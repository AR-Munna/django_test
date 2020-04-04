from django.shortcuts import render
from .models import Album
from django.http import HttpResponse, Http404


def index(request):
    all_albums = Album.objects.all()
    context = {'all_albums': all_albums}
    return render(request, 'index.html', context)


def details(request, album_id):
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Album does not exist :(")
    return render(request, 'details.html', {'album': album})
