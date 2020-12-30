from datetime import datetime
from socket import gethostname

from django.http import JsonResponse

from .models import Visit


def home(request):
    new_visit = Visit.objects.create(
        user_browser=request.META['HTTP_USER_AGENT'],
        user_ip=request.META['REMOTE_ADDR'],
    )

    return JsonResponse({
        'message': 'hello world',
        'answer': 42,
        'server': gethostname(),
        'time': datetime.now(),
        'visit_counter': Visit.objects.count(),
    })
