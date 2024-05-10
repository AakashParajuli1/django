from django.http import HttpResponse
from django.shortcuts import render
def homePage(request):
    data = {
        'title' : 'Home page',
        'bdata' : 'Euta manche ko maya',
        'clist' : ['php', 'java', 'c++'],
        'student_details' : [
            {'name' : 'abc', 'phone' : '6666666'},
            {'name' : 'xyz', 'phone' : '9999999'}
        ]
    }
    return render(request, "index.html", data)


def aboutus(request):
    return HttpResponse("Welcome to second project")


def index(request):
    return HttpResponse("Welcome to the homepage of second project.")