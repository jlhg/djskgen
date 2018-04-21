import random

from django.shortcuts import render


def index(request):
    if request.method == 'POST':
        secret_keys = {}
        key_id = 1
        for i in range(20):
            secret_keys.update({key_id: ''.join([random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for _ in range(50)])})
            key_id += 1

        return render(request,
                      'djskgen/index.html',
                      {
                          'secret_keys': secret_keys,
                      },
                      )
    else:
        return render(request,
                      'djskgen/index.html',
                      )