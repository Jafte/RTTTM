from django.views.generic import ListView, DetailView, CreateView, UpdateView, FormView, RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin
from sound.models import Sound, Author, Request, ArtistRequest
from sound.forms import RequestForm
from django.http import Http404
from django.shortcuts import get_object_or_404
from pure_pagination.mixins import PaginationMixin


class AuthorList(PaginationMixin, ListView):
    model = Author
    template_name = "sound/author_list.html"
    context_object_name = "author_list"
    paginate_by = 40


class AuthorDetail(DetailView):
    model = Author
    template_name = "sound/author_detail.html"
    context_object_name = "author"


class AuthorUpdate(LoginRequiredMixin, UpdateView):
    model = Author
    template_name = "sound/author_form.html"
    fields = ["name", "about", "photo"]

    def dispatch(self, request, *args, **kwargs):
        author = self.get_object()
        if request.user != author.user:
            raise Http404()
        return super(AuthorUpdate, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(AuthorUpdate, self).get_context_data(**kwargs)
        context["author"] = self.get_object()

        return context

    def get_success_url(self):
        author = self.get_object()
        return author.get_absolute_url()


class SoundList(PaginationMixin, ListView):
    model = Sound
    template_name = "sound/sound_list.html"
    context_object_name = "sound_list"
    paginate_by = 40


class SoundDetail(DetailView):
    model = Sound
    template_name = "sound/sound_detail.html"
    context_object_name = "sound"


class RequestList(PaginationMixin, ListView):
    model = Request
    template_name = "sound/request_list.html"
    context_object_name = "request_list"
    paginate_by = 40


class RequestDetail(DetailView):
    model = Request
    template_name = "sound/request_detail.html"
    context_object_name = "request_object"

    def get_context_data(self, **kwargs):
        context = super(RequestDetail, self).get_context_data(**kwargs)
        request_object = self.get_object()
        user = self.request.user

        artist_requests = ArtistRequest.objects.filter(request=request_object, status__lte=1)
        context["artist_requests"] = artist_requests
        if user.profile.is_voice_artist:
            user_artist_requests = artist_requests.filter(voice__in=user.voices.all())
            user_voices_in = []
            for ar in user_artist_requests:
                user_voices_in.append(ar.voice)
            context["user_voices_in"] = user_voices_in

        return context


class RequestGetIn(LoginRequiredMixin, RedirectView):
    sound_request = False
    voice = False

    def get_sound_request(self):
        if not self.sound_request:
            self.sound_request = get_object_or_404(Request, pk=self.kwargs.get('request_pk'))
        return self.sound_request

    def get_voice(self):
        if not self.voice:
            self.voice = get_object_or_404(Author, pk=self.kwargs.get('voice_pk'))
        return self.voice

    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if not user.profile.is_voice_artist:
            raise Http404()
        return super(RequestGetIn, self).dispatch(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        sound_request = self.get_sound_request()
        voice = self.get_voice()
        user = self.request.user

        if not voice.check_request_already_gated_in(sound_request):
            ar = ArtistRequest()
            ar.voice = voice
            ar.request = sound_request
            ar.status = 0
            ar.save()

        return sound_request.get_absolute_url()


class RequestGetOut(LoginRequiredMixin, RedirectView):
    sound_request = False
    voice_sound_request = False

    def get_sound_request(self):
        if not self.sound_request:
            self.sound_request = get_object_or_404(Request, pk=self.kwargs.get('request_pk'))
        return self.sound_request

    def get_voice_sound_request(self):
        if not self.voice_sound_request:
            self.voice_sound_request = get_object_or_404(ArtistRequest, pk=self.kwargs.get('voice_pk'), status__lte=1)
        return self.voice_sound_request

    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if not user.profile.is_voice_artist:
            raise Http404()
        return super(RequestGetOut, self).dispatch(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        sound_request = self.get_sound_request()
        voice_sound_request = self.get_voice_sound_request()
        voice_sound_request.status = 9
        voice_sound_request.save()

        return sound_request.get_absolute_url()


class RequestCreate(LoginRequiredMixin, CreateView):
    model = Request
    template_name = "sound/request_form.html"
    form_class = RequestForm

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        form.instance.status = 0

        return super(RequestCreate, self).form_valid(form)
