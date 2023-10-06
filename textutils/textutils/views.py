# created
from django.http import HttpResponse


def index(request):
    return HttpResponse("Home")


def removepunc(request):
    return HttpResponse("remove punc")


def capfirst(request):
    return HttpResponse("capitalize first")
