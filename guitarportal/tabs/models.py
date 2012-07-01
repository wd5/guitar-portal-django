from django.db import models

from taggit.managers import TaggableManager
from django.db.models.aggregates import Max

class Artist(models.Model):
    """Represents the artist in database."""
    name = models.CharField(max_length=100)
    albums = models.ManyToManyField('Album')
    home_page = models.URLField(max_length=200)
    tags = TaggableManager()

    def __unicode__(self):
        return self.name


class Album(models.Model):
    """Represents a single album."""
    title = models.CharField(max_length=100)
    songs = models.ManyToManyField('Song')
    tags = TaggableManager()

    def __unicode__(self):
        return self.title


class Song(models.Model):
    """Represents a song in database."""
    track_number = models.PositiveSmallIntegerField()
    title = models.CharField(max_length=200)
    artists = models.ManyToManyField('Artist')
    tags = TaggableManager()

    #class Meta:
    #    unique_together = (('track_number', 'title', 'album'))

    def __unicode__(self):
        return self.title


class SongRepresentation(models.Model):
    """Represents a song in some way recognizable by human - a tab, a list of
    chords, notes, and so on."""
    version = models.PositiveSmallIntegerField(blank=True, null=True, editable=False)
    song = models.ForeignKey(Song)
    
    class Meta:
        """We define this model as abstract - we don't want to
        instantiate it"""
        abstract = True

    def save(self, *args, **kwargs):
        """Saves object in the database.
        Overriden for version incrementation.
        """
        self.version = SongRepresentation.objects.filter(song=self.song).\
                            aggregate(
                                Max('version')
                            ) + 1
        super(SongRepresentation, self).save(*args, **kwargs)

    def __unicode__(self):
        return '{} (version {}, {})'.format(
                    str(self.song), self.version, type(self).__name__)


class Chord(SongRepresentation):
    """Extends SongRepresentation model. Used to distinguish chords from
    other song representations."""
    ascii_res = models.TextField()


class Tab(SongRepresentation):
    """Extends SongRepresentation model. Used to distinguish tabs from
    other song representations."""
    ascii_res = models.TextField()


class GuitarPro(SongRepresentation):
    """Extends SongRepresentation model. Used to distinguish Guitar Pro files
    from other song representations."""
    pro_file = models.FilePathField()

    class Meta(SongRepresentation.Meta):
        verbose_name = "Guitar Pro file"
        verbose_name_plural = "Guitar Pro files"
