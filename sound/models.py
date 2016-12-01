from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from uuid_upload_path import upload_to
from django.urls import reverse
from text.models import Text

STATUS_CHOICES = (
    (1, _('New')),
    (2, _('Done')),
    (3, _('Double')),
    (4, _('Reject')),
    (5, _('In progress')),
)


class Author(models.Model):
    name = models.CharField(verbose_name=_('name'), max_length=200)
    about = models.TextField(verbose_name=_('about'), blank=True)
    user = models.ForeignKey(to=User, null=True, blank=True)

    def __str__(self):
        return '%s' % self.name

    def get_absolute_url(self):
        return reverse('sound-author-detail', kwargs={'pk': self.pk})


class Request(models.Model):
    user = models.ForeignKey(to=User, related_name="created_requests")
    title = models.CharField(verbose_name=_('title'), max_length=200)
    url_to_source = models.CharField(verbose_name=_('url to source'), blank=True, max_length=200)
    text_source = models.TextField(verbose_name=_('text source'), blank=True)
    description = models.TextField(verbose_name=_('description'), blank=True)
    status = models.PositiveSmallIntegerField(_('status'), choices=STATUS_CHOICES, blank=True)
    text = models.ForeignKey(to=Text, blank=True, null=True, related_name="requests")
    created = models.DateTimeField(verbose_name=_('created'), auto_now_add=True)
    taken_by_users = models.ManyToManyField(to=User, through='ArtistRequest', related_name="taken_requests")

    def __str__(self):
        return '%s request from %s' % (self.title, self.user)

    def get_absolute_url(self):
        return reverse('request-detail', kwargs={'pk': self.pk})


class ArtistRequest(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    request = models.ForeignKey(to=Request, on_delete=models.CASCADE)
    created = models.DateTimeField(verbose_name=_('created'), auto_now_add=True)
    status = models.PositiveSmallIntegerField(_('status'), choices=STATUS_CHOICES, blank=True)

    def __str__(self):
        return '%s request taken by %s' % (self.title.request, self.user)

    def get_absolute_url(self):
        return reverse('request-detail', kwargs={'pk': self.request.pk})


class Sound(models.Model):
    text = models.ForeignKey(to=Text, verbose_name=_('text'), related_name="sounds")
    author = models.ForeignKey(to=Author, verbose_name=_('author'), related_name="sounds")
    file = models.FileField(verbose_name=_('file'), upload_to=upload_to)
    created = models.DateTimeField(verbose_name=_('created'), auto_now_add=True)
    modified = models.DateTimeField(verbose_name=_('modified'), auto_now=True)
    request = models.ForeignKey(to=Request, blank=True, null=True)

    def __str__(self):
        return '%s sounded by %s' % (self.text, self.author)

    def get_absolute_url(self):
        return reverse('sound-detail', kwargs={'pk': self.pk})

    def get_other_sounds(self):
        return Sound.objects.filter(text=self.text).exclude(pk=self.pk)
