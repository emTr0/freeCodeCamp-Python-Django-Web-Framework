from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home_view(request, *args, **kwargs):  # *args, **kwargs
    # return HttpResponse("<h1>Hello World</h1>")  # string of HTML code
    return render(request, "home.html", {})


def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})


def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": "This is about us",
        "this_is_true": True,
        "my_number": 123,
        "my_list": [123, 456, 312, "Abc"]
    }
    return render(request, "about.html", my_context)
