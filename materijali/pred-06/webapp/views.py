from django.http import JsonResponse

from datetime import datetime
from socket import gethostname


def home(request):
    return JsonResponse({
        'message': 'hello world',
        'answer': 42,
        'server': gethostname(),
        'time': datetime.now(),
    })
