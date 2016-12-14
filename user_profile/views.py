from django.views.generic import ListView, DetailView, FormView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.http import Http404
from .forms import ProfileForm


class UserDetail(DetailView):
    slug_field = 'username'
    context_object_name = "user_data"
    slug_url_kwarg = 'username'
    queryset = User.objects.filter(is_active=True)
    template_name = 'user_profile/user_detail.html'


class UserEdit(LoginRequiredMixin, FormView):
    slug_url_kwarg = 'username'
    form_class = ProfileForm
    template_name = 'user_profile/user_edit.html'
    user = None

    def dispatch(self, request, *args, **kwargs):
        user = self.get_user()
        if request.user != user:
            raise Http404()

        return super(UserEdit, self).dispatch(request, *args, **kwargs)

    def get_user(self):
        if not self.user:
            slug = self.kwargs.get(self.slug_url_kwarg)
            self.user = get_object_or_404(User, username=slug)

        return self.user

    def get_initial(self):
        initial = super(UserEdit, self).get_initial()

        user = self.get_user()

        if user.first_name and user.last_name:
            initial['name'] = "%s %s" % (user.first_name, user.last_name)
        else:
            initial['name'] = "%s" % user.first_name

        initial['about'] = user.profile.about
        initial['photo'] = user.profile.photo

        return initial

    def get_context_data(self, **kwargs):
        context = super(UserEdit, self).get_context_data()

        user = self.get_user()

        context["user_data"] = user

        return context

    def form_valid(self, form):
        user = self.get_user()

        name = form.cleaned_data["name"].split(" ", 1)
        user.first_name = ""
        user.last_name = ""
        if len(name) > 1:
            user.first_name = name[0]
            user.last_name = name[1]
        else:
            user.first_name = name[0]

        user.save()

        user.profile.about = form.cleaned_data["about"]
        user.profile.photo = form.cleaned_data["photo"]
        user.profile.save()

        return redirect('user-profile-detail', username=user.username)


class UserList(ListView):
    queryset = User.objects.filter(is_active=True)
    template_name = 'user_profile/user_list.html'
