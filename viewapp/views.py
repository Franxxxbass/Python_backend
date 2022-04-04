from django.shortcuts import HttpResponse, render
from django import views


# function-based view
def hello(request):
    return HttpResponse("elo łorld!")


# class-based view
class HelloView(views.View):
    def get(self, request):
        return HttpResponse("eloł łorlt!")

# functional-based view
def hello_template(request):
    return render(
        request,
        'viewapp/hello.html'
    )

# class-based view
class HelloClassicView(views.View):
    def get(self, request):
        return render(
            request,
            'viewapp/hello.html'
        )

