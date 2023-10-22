from django.shortcuts import render

from .utils import get_mongodb

def main(request):
    db = get_mongodb()
    quotes = db.quotes.find({}).limit(3)
    context = {"quotes": quotes}
    return render(request, "quotes/index.html", context)
