from django.contrib import admin
from text.models import Text, Author, Category


admin.site.register(Category)
admin.site.register(Text)
admin.site.register(Author)