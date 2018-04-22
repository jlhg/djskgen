from random import SystemRandom

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


def _generate_secret_keys():
    system_random = SystemRandom()
    allowed_chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    return [
        ''.join([system_random.choice(allowed_chars) for _ in range(50)])
        for _ in range(1, 21)
    ]


def index(request):
    method = request.method.upper()

    if method not in ['GET', 'POST']:
        return HttpResponse(status=405)

    if method == 'POST':
        secret_keys = _generate_secret_keys()
        return JsonResponse(secret_keys, safe=False)

    return render(request, 'index.html')
