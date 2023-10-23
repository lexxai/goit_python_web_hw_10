from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Quote, Author, Tag


PER_PAGE = 2

# def main_mongodb_version(request, page=1):
#     from .utils import get_mongodb
#     db = get_mongodb()
#     quotes = db.quotes.find({}).limit(15)
#     paginator = Paginator(list(quotes), per_page=PER_PAGE)

#     context = {"quotes": paginator.page(page)}
#     return render(request, "quotes/index.html", context)


def main(request, page=1):
    quotes = Quote.objects.all()
    paginator = Paginator(list(quotes), per_page=PER_PAGE)

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
    quotes = Tag.objects.get(name=tag)
    paginator = Paginator(list(quotes), per_page=PER_PAGE)

    context = {"tag": paginator.page(page)}
    return render(request, "quotes/tag.html", context)
