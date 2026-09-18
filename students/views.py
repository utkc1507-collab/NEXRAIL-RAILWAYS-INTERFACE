from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1>Welcome to Student Home Page</h1>")


def profile(request):
    return HttpResponse("Student Profile Page")


def courses(request):
    return HttpResponse("Student Courses Page")