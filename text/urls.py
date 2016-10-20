from django.conf.urls import url
from text.views import AuthorDetail, AuthorList, TextDetail, TextList

urlpatterns = [
    url(r'^author/(?P<pk>[\d]+)/$', AuthorDetail.as_view(), name="text-author-detail"),
    url(r'^author/$', AuthorList.as_view(), name="text-author-list"),
    url(r'^(?P<pk>[\d]+)/$', TextDetail.as_view(), name="text-detail"),
    url(r'^$', TextList.as_view(), name="text-list"),
]