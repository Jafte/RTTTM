from django.conf.urls import url
from sound.views import AuthorDetail, AuthorList, SoundDetail, SoundList, RequestDetail, RequestList

urlpatterns = [
    url(r'^author/(?P<pk>[\d]+)/$', AuthorDetail.as_view(), name="sound-author-detail"),
    url(r'^author/$', AuthorList.as_view(), name="sound-author-list"),
    url(r'^req/(?P<pk>[\d]+)/$', RequestDetail.as_view(), name="request-detail"),
    url(r'^req/$', RequestList.as_view(), name="request-list"),
    url(r'^(?P<pk>[\d]+)/$', SoundDetail.as_view(), name="sound-detail"),
    url(r'^$', SoundList.as_view(), name="sound-list"),
]