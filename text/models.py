from django.db import models
from django.utils.translation import ugettext_lazy as _
from easy_thumbnails.fields import ThumbnailerImageField
from uuid_upload_path import upload_to
from django.urls import reverse


class Author(models.Model):
    name = models.CharField(verbose_name=_('name'), max_length=200)
    about = models.TextField(verbose_name=_('about'), blank=True)
    photo = ThumbnailerImageField(verbose_name=_('photo'), upload_to=upload_to, blank=True)

    def __str__(self):
        return '%s' % self.name

    def get_absolute_url(self):
        return reverse('text-author-detail', kwargs={'pk': self.pk})


class Text(models.Model):
    name = models.CharField(verbose_name=_('name'), max_length=200)
    url_to_source = models.CharField(verbose_name=_('url to source'), blank=True, max_length=200)
    text = models.TextField(verbose_name=_('text'))
    author = models.ForeignKey(to=Author, verbose_name=_('author'), related_name="texts")
    created = models.DateTimeField(verbose_name=_('created'), auto_now_add=True)
    modified = models.DateTimeField(verbose_name=_('modified'), auto_now=True)

    def __str__(self):
        return '%s (%s)' % (self.name, self.author)

    def get_absolute_url(self):
        return reverse('text-detail', kwargs={'pk': self.pk})
