"""views"""

import pdb
from django.http import HttpResponse, JsonResponse
from datetime import datetime


def hello_world(request):
    now = datetime.now().strftime("%b %dth, %Y - %H:%M hrs")
    return HttpResponse(f"Current Server time is : {str(now)}")


def hi(request):
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    # pdb.set_trace()
    # numbers = set(numbers)
    return JsonResponse({"numbers": numbers,
                         "sorted_numbers": sorted(numbers)})