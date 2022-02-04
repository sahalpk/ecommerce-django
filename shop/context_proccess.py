from os import link
from typing import Dict
from .models import Category


def menu_links(request):
    Links = Category.objects.all()
    return dict(Links=Links)
