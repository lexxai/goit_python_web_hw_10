from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Quote, Author, Tag


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
    context = {"quotes": paginator.page(page), "tag_query":tag}
    return render(request, "quotes/tag.html", context)


    tag = Tag.objects.get(name=tag)
    paginator = Paginator(tag, per_page=PER_PAGE)

    context = {"tag": paginator.page(page)}
    return render(request, "quotes/tag.html", context)
