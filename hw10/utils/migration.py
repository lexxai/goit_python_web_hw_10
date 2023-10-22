import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hw10.settings")

django.setup()

from quotes.models import Quote, Tag, Author #noqa
from quotes.utils import get_mongodb 

def import_records():
    db = get_mongodb()
    authors = db.authors.find()
    
    for author in authors:
        author_data = {
            "fullname": author["fullname"],
            "born_date": author["born_date"],
            "born_location": author["born_location"],
            "description": author["description"]
        }
        Author.objects.get_or_create(**author_data)

    quotes = db.quotes.find()
    tags = set()
    for quote in quotes:
        for tag in quote.get("tags"):
            if tag:
                tags.add(tag)

    tags_obj = []
    for tag in tags:
        # print(f"{tag=}")
        t, *_ = Tag.objects.get_or_create(name=tag)
        tags_obj.append(t)
    
    # print(tags_obj)


if __name__ == "__main__":
    import_records()

 

