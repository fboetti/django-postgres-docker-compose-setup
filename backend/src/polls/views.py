from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse


def index(request: WSGIRequest):
    print(request.content_type)
    return HttpResponse("Hello, world. You're at the polls index.")
