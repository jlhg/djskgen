from random import SystemRandom

from django.http import HttpResponse
from django.shortcuts import render


def _generate_secret_keys():
    system_random = SystemRandom()
    allowed_chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    return {
        key_id: ''.join([system_random.choice(allowed_chars) for _ in range(50)])
        for key_id in range(1, 21)
    }


def index(request):
    method = request.method.upper()

    context = {}

    if method not in ['GET', 'POST']:
        return HttpResponse(status=405)

    if method == 'POST':
        context['secret_keys'] = _generate_secret_keys()

    return render(request, 'djskgen/index.html', context)
