from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.core.validators import URLValidator

from .models import URL

import string
import random
# Create your views here.


characters = string.ascii_letters + string.digits


def generate_key():
    return "".join(random.choice(characters) for _ in range(random.randint(6, 10)))


@csrf_protect
def index(request):
    if request.method == "POST":
        context = {}
        # Check if url is valid
        if request.POST["url"]:
            try:
                validate = URLValidator()
                validate(request.POST["url"])
            except ValidationError:
                context["error"] = "Invalid url"
                context["url"] = request.POST["url"]
                return render(request, "shortener/index.html", context)
        else:
            context["error"] = "Put the url"
            return render(request, "shortener/index.html", context)

        # Add url to db
        saved = False
        while saved == False:
            key = generate_key()
            try:
                    obj = URL.objects.get(key=key)
            except ObjectDoesNotExist:
                    obj = URL(url=request.POST["url"], key=key)
                    obj.save()
                    saved = True
                    context["key"] = key
                    context["host"] = request.get_host()
        return render(request, "shortener/detail.html", context)

    return render(request, "shortener/index.html")


def goto(request, key):
    try:
            obj = URL.objects.get(key=key)
            return redirect(obj.url)
    except ObjectDoesNotExist:
            return redirect("/")
