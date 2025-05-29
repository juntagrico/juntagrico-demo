from time import sleep

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


@login_required
def timeout(request, duration):
    sleep(duration)
    return HttpResponse(f'{duration}s')
