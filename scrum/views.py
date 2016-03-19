from django.http import HttpResponse


def index(request):
    return HttpResponse("MILL - a lightweight web app for Scrum development")
