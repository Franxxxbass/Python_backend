from markupsafe import escape

from django.shortcuts import HttpResponse, render



def hello(request):
    return HttpResponse('Eluwinka')

def hello2(request):

    return render(
        request,
        'intro/hello.html',
    )

def hello3(request):
    content = '<!DOCUMENT html><html><head><body><h1>Witaj świecie'
    return HttpResponse(content)

def adam(request):
    return HttpResponse('siema adasko')

def ewa(request):
    return HttpResponse('siema ewunia!')

def name_view(request, name): #musi byc po requescie, bo przekazalismy w urlpatterins str:name
    msg = f'siema {name.title()}'
    sanitize_msg = escape(meg)
    return HttpResponse(sanitize_msg)

def card(request):
    return render(
        request,
        'intro/card.html',
    )

def name_view_2(request, name):
    return render(
        request,
        'intro/hello2.html',
        context = {
            "name": name
        }
    )