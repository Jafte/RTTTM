from django.views.generic import TemplateView
from sound.models import Sound, Author, Request


class IndexPage(TemplateView):
    template_name = "app/index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexPage, self).get_context_data(**kwargs)
        context["last_sounds"] = Sound.objects.all()[:10]

        return context