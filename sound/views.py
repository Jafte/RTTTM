from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from sound.models import Sound, Author, Request
from sound.forms import RequestForm


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
    context_object_name = "sound_list"


class SoundDetail(DetailView):
    model = Sound
    template_name = "sound/sound_detail.html"
    context_object_name = "sound"


class RequestList(ListView):
    model = Request
    template_name = "sound/request_list.html"
    context_object_name = "request_list"


class RequestDetail(DetailView):
    model = Request
    template_name = "sound/request_detail.html"
    context_object_name = "request_object"


class RequestCreate(LoginRequiredMixin, CreateView):
    model = Request
    template_name = "sound/request_form.html"
    form_class = RequestForm

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        form.instance.status = 1

        return super(RequestCreate, self).form_valid(form)
