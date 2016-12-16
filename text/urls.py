from django.conf.urls import url
from text.views import AuthorDetail, AuthorList, TextDetail, TextList, CategoryTextList

urlpatterns = [
    url(r'^author/(?P<pk>[\d]+)/$', AuthorDetail.as_view(), name="text-author-detail"),
    url(r'^author/$', AuthorList.as_view(), name="text-author-list"),
    url(r'^i(?P<pk>[\d]+)/$', TextDetail.as_view(), name="text-detail"),
    url(r'^(?P<category_slug>[\w]+)/$', CategoryTextList.as_view(), name="text-category"),
    url(r'^$', TextList.as_view(), name="text-list"),
]