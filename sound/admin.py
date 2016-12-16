from django.contrib import admin
from sound.models import Sound, Author, Request, ArtistRequest


class ArtistRequestInline(admin.TabularInline):
    model = ArtistRequest
    extra = 1


class RequestAdmin(admin.ModelAdmin):
    inlines = (ArtistRequestInline,)


admin.site.register(Sound)
admin.site.register(Author)
admin.site.register(Request, RequestAdmin)
