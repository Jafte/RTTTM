from django.conf.urls import url
from sound.views import AuthorDetail, AuthorList, AuthorUpdate, \
    SoundDetail, SoundList, \
    RequestDetail, RequestGetOut, RequestGetIn, RequestList, RequestCreate

urlpatterns = [
    url(r'^author/(?P<pk>[\d]+)/edit/$', AuthorUpdate.as_view(), name="sound-author-update"),
    url(r'^author/(?P<pk>[\d]+)/$', AuthorDetail.as_view(), name="sound-author-detail"),
    url(r'^author/$', AuthorList.as_view(), name="sound-author-list"),
    url(r'^req/add/$', RequestCreate.as_view(), name="request-create"),
    url(r'^req/(?P<request_pk>[\d]+)/get-out/(?P<pk>[\d]+)/$', RequestGetOut.as_view(), name="request-author-get-out"),
    url(r'^req/(?P<request_pk>[\d]+)/get-in/(?P<pk>[\d]+)/$', RequestGetIn.as_view(), name="request-author-get-in"),
    url(r'^req/(?P<pk>[\d]+)/$', RequestDetail.as_view(), name="request-detail"),
    url(r'^req/$', RequestList.as_view(), name="request-list"),
    url(r'^(?P<pk>[\d]+)/$', SoundDetail.as_view(), name="sound-detail"),
    url(r'^$', SoundList.as_view(), name="sound-list"),
]
