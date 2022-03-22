
from django.shortcuts import render
import random

def toto_lotek(request):

    numbers = random.sample(range(1, 49), 6)

    return render(
        request,
        'draw/toto-lotek.html',
        context={
            "numbers": numbers
        }
    )