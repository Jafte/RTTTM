from django.views.generic import ListView, DetailView
from sound.models import Sound, Author, Request


class AuthorList(ListView):
    model = Author
    template_name = "sound/author_list.html"
    context_object_name = "author_list"


class AuthorDetail(DetailView):
    model = Author
    template_name = "sound/author_detail.html"
    context_object_name = "author"


class SoundList(ListView):
    model = Sound
    template_name = "sound/sound_list.html"
    context_object_name = "text_list"


class SoundDetail(DetailView):
    model = Sound
    template_name = "sound/sound_detail.html"
    context_object_name = "text"


class RequestList(ListView):
    model = Request
    template_name = "sound/request_list.html"
    context_object_name = "text_list"


class RequestDetail(DetailView):
    model = Request
    template_name = "sound/request_detail.html"
    context_object_name = "text"
