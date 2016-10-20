from django.views.generic import ListView, DetailView
from text.models import Text, Author


class AuthorList(ListView):
    model = Author
    template_name = "text/author_list.html"
    context_object_name = "author_list"


class AuthorDetail(DetailView):
    model = Author
    template_name = "text/author_detail.html"
    context_object_name = "author"


class TextList(ListView):
    model = Text
    template_name = "text/text_list.html"
    context_object_name = "text_list"


class TextDetail(DetailView):
    model = Text
    template_name = "text/text_detail.html"
    context_object_name = "text"
