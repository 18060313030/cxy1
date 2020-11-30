import django.http import HttpResponse


def index(request):
    return HttpResponse("hah")


def login(request):
    return redirect("/login.html")
