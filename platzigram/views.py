"""views"""

import pdb
from django.http import HttpResponse, JsonResponse
from datetime import datetime


def hello_world(request):
    now = datetime.now().strftime("%b %dth, %Y - %H:%M hrs")
    return HttpResponse(f"Current Server time is : {str(now)}")


def sort_integers(request):
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    # pdb.set_trace()
    # numbers = set(numbers)
    return JsonResponse({"numbers": numbers,
                         "sorted_numbers": sorted(numbers)})


def say_hi(request, name, age):
    if age <= 17:
        message = f'Sorry {name} this is a page not for childs and teenagers :v'
    else:
        message = f'Welcome to my page {name}'
    return HttpResponse(message)