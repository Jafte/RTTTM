from django.views.generic import ListView, DetailView
from text.models import Text, Author, Category
from django.shortcuts import get_object_or_404
from pure_pagination.mixins import PaginationMixin


class AuthorList(PaginationMixin, ListView):
    model = Author
    template_name = "text/author_list.html"
    context_object_name = "author_list"
    paginate_by = 40


class AuthorDetail(DetailView):
    model = Author
    template_name = "text/author_detail.html"
    context_object_name = "author"


class TextList(PaginationMixin, ListView):
    model = Text
    template_name = "text/text_list.html"
    context_object_name = "text_list"
    paginate_by = 40

    def get_context_data(self, **kwargs):
        context = super(TextList, self).get_context_data(**kwargs)
        context["last_authors"] = Author.objects.all()[:12]
        context["categories"] = Category.objects.all()

        return context


class TextDetail(DetailView):
    model = Text
    template_name = "text/text_detail.html"
    context_object_name = "text"


class CategoryTextList(PaginationMixin, ListView):
    model = Text
    template_name = "text/text_list.html"
    context_object_name = "text_list"
    category = False
    paginate_by = 40

    def get_category(self):
        if not self.category:
            self.category = get_object_or_404(Category, slug=self.kwargs.get('category_slug'))
        return self.category

    def get_queryset(self):
        category = self.get_category()
        return category.texts.all()

    def get_context_data(self, **kwargs):
        context = super(CategoryTextList, self).get_context_data(**kwargs)
        category = self.get_category()
        context["categories"] = Category.objects.all()
        context["current_category"] = category

        return context
