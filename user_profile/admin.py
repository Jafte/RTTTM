from django.contrib import admin
from user_profile.models import Profile, VoiceRequest

admin.site.register(Profile)
admin.site.register(VoiceRequest)