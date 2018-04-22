from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from core.helpers import generate_secret_key


def index(request):
    method = request.method.upper()

    if method not in ['GET', 'POST']:
        return HttpResponse(status=405)

    if method == 'POST':
        secret_keys = [generate_secret_key() for _ in range(1, 21)]
        return JsonResponse(secret_keys, safe=False)

    return render(request, 'index.html')
