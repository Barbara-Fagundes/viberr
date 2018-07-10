from django.db import models

class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)

    def __str__(self):
        return self.album_title + ' - ' + self.artist
        # This will list the content whenever you call Album.objects.all() in the power shell

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title

# No migration is needed unless you change the attributes or add attributes in the class.
# Because it changes the structure of your database. HOWEVER if you create a new class, no migration is needed
# because it doesn't change the structure of your database.
# Example of class above: class Song. Example of its attribute: file_type = bla bla...

# TO DO MIGRATION:
# go to the console (Power Shell)
# type: python manage.py makemigrations music
# after doing that your database will be up to date with the new changes u did!
# AFTER doing all the steps above, you need to restart the server!