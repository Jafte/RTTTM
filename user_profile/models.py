from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from easy_thumbnails.fields import ThumbnailerImageField
from uuid_upload_path import upload_to
from django.urls import reverse

from django.db.models.signals import post_save
from sound.models import Author


class Profile(models.Model):
    """ Default profile """

    user = models.OneToOneField(User, unique=True, verbose_name=_('user'), related_name='profile') 
    about = models.TextField(_('about me'), blank=True)
    photo = ThumbnailerImageField(verbose_name=_('photo'), upload_to=upload_to, blank=True)
    is_voice_artist = models.BooleanField(_('is voice artist'), default=False)

    def get_absolute_url(self):
        return reverse('user-profile-detail', kwargs={'username': self.user.username})

    def __str__(self):
        return '%s profile' % self.user


class VoiceRequest(models.Model):
    user = models.ForeignKey(User)
    message = models.TextField()
    response = models.TextField(blank=True)
    created = models.DateTimeField(verbose_name=_('created'), auto_now_add=True)
    modified = models.DateTimeField(verbose_name=_('modified'), auto_now=True)


def user_changed(sender, **kwargs):
    user = kwargs["instance"]
    if hasattr(user, 'profile'):
        pass
    else:
        profile = Profile(user=user)
        profile.save()

post_save.connect(user_changed, sender=User)