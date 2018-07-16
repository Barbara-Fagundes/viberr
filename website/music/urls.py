from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    # /music/
    path('', views.IndexView.as_view(), name='index'),  #each url path needs to be hooked to a view function -- Before this line was:--> path('', views.index, name='index'),

    # /music/<album_id>/
    path('<int:pk>[0-9]+)/', views.DetailView.as_view(), name='detail'), #whenever we're using detail view, it requires the primary key
    # path('<int:album_id>[0-9]+)/', views.detail, name='detail'),

    # /music/album/add/
    path('album/add/$', views.AlbumCreate.as_view(), name='album-add'),

# /music/album/2/
    path('<int:pk>[0-9]+)/', views.AlbumUpdate.as_view(), name='album-update'),

# /music/album/2/delete/
    path('<int:pk>[0-9]+)/delete/', views.AlbumDelete.as_view(), name='album-delete'),

]
    # /music/<album_id>/favorite/
  #  path('<int:album_id>[0-9]+)favorite/', views.favorite, name='favorite'), (Not using this line anymore)

#music/2[0-9]+)/{ url 'music:detail' album.id %