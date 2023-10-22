from django.shortcuts import render
from django.core.paginator import Paginator

from .utils import get_mongodb

PER_PAGE = 2

def main(request, page=1):
    db = get_mongodb()
    quotes = db.quotes.find({}).limit(15)
    paginator = Paginator(list(quotes), per_page=PER_PAGE)

    context = {"quotes": paginator.page(page)}
    return render(request, "quotes/index.html", context)
