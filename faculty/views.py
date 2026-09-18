from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1>Welcome to Faculty Home Page</h1>")


def profile(request):
    return HttpResponse("Faculty Profile Page")