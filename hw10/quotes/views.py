from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views import View
from django.contrib import messages
from django.contrib.auth.models import User

from .models import Quote, Author, Tag

from .froms import AuthorForm


PER_PAGE = 4

# def main_mongodb_version(request, page=1):
#     from .utils import get_mongodb
#     db = get_mongodb()
#     quotes = db.quotes.find({}).limit(15)
#     paginator = Paginator(list(quotes), per_page=PER_PAGE)

#     context = {"quotes": paginator.page(page)}
#     return render(request, "quotes/index.html", context)


def main(request, page=1):
    quotes = Quote.objects.all()
    paginator = Paginator(quotes, per_page=PER_PAGE)

    context = {"quotes": paginator.page(page)}
    return render(request, "quotes/index.html", context)


def author(request, author: str):
    try:
        author = Author.objects.get(fullname=author)
    except:
        author = None
    context = {"author": author}
    return render(request, "quotes/author.html", context)


def tag(request, tag: str, page: int = 1):
    quotes = []
    tag_id = None
    try:
        tag_id = Tag.objects.get(name=tag).id
    except:
        ...
    print(f"{tag=},{tag_id=}")
    if tag_id:
        quotes = Quote.objects.filter(tags=tag_id)

    paginator = Paginator(quotes, per_page=PER_PAGE)
    context = {"quotes": paginator.page(page), "tag_query": tag}
    return render(request, "quotes/tag.html", context)

    tag = Tag.objects.get(name=tag)
    paginator = Paginator(tag, per_page=PER_PAGE)

    context = {"tag": paginator.page(page)}
    return render(request, "quotes/tag.html", context)


@login_required
def add_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            fullname = form.cleaned_data["fullname"]
            messages.success(request, f"Author '{fullname}' was created...")
            return render(
                request, "quotes/add_author.html", context={"form": AuthorForm()}
            )
        else:
            messages.error(request, "Not added...")
            return render(request, "quotes/add_author.html", context={"form": form})

    context = {"form": AuthorForm()}
    return render(request, "quotes/add_author.html", context)


class AddAuthorView(LoginRequiredMixin, View):
    form_class = AuthorForm
    template_name = "quotes/add_author.html"

    def get(self, request):
        return render(request, self.template_name, context={"form": self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            fullname = form.cleaned_data["fullname"]
            messages.success(request, f"Author '{fullname}' was created...")
            return render(
                request, self.template_name, context={"form": self.form_class}
            )
        else:
            messages.error(request, "Not added...")
            return render(request, self.template_name, context={"form": form})
