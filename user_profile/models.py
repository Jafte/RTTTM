from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.urls import reverse

from django.db.models.signals import post_save


class Profile(models.Model):
    """ Default profile """

    user = models.OneToOneField(User, unique=True, verbose_name=_('user'), related_name='profile') 
    about = models.TextField(_('about me'), blank=True)

    def get_absolute_url(self):
        return reverse('user-profile-detail', kwargs={'username': self.user.username})

    def __str__(self):
        return '%s profile' % self.user


def user_changed(sender, **kwargs):
    user = kwargs["instance"]
    if hasattr(user, 'profile'):
        pass
    else:
        profile = Profile(user=user)
        profile.save()

post_save.connect(user_changed, sender=User)