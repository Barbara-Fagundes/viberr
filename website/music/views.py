# from django.http import Http404 we can delete it bz we re not using it anymore since we replaced the try exception
# from django.http import HttpResponse

from django.shortcuts import render, get_object_or_404
from .models import Album, Song


def index(request):
    all_albums = Album.objects.all()
    # template = loader.get_template('music/index.html')
    return render(request, 'music/index.html', {'all_albums': all_albums})
    # HttpResponse(template.render(context, request))

def detail(request,album_id):
    album = get_object_or_404(Album, pk=album_id) #this is more convenient than try exception below in the comments
    return render(request, 'music/detail.html', {'album': album})

def favorite(request,album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except (KeyError, Song.DoesNotExist):
        return render(request, 'music/detail.html', {
            'album': album,
            'error_message': "You did not select a valid song",
        })
    else:
        selected_song.is_favorite = True
        selected_song.save()
        return render(request, 'music/detail.html', {'album': album})

# def detail(request,album_id):   # return HttpResponse("<h2> Details for Album id: " + str(album_id) + "</h2>")
#     try:
#         album = Album.objects.get(pk=album_id)
#     except Album.DoesNotExist:
#         raise Http404("Album does not exist")
#     return render(request, 'music/detail.html', {'album': album})