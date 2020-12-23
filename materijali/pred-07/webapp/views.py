from django.http import JsonResponse

from datetime import datetime
from socket import gethostname


def home(request):

    new_visit = {
        'visit_time': datetime.now(),
        'user_browser': request.META['HTTP_USER_AGENT'],
        'user_ip': request.META['REMOTE_ADDR'],
    }

    return JsonResponse({
        'message': 'hello world',
        'answer': 42,
        'server': gethostname(),
        'time': datetime.now(),
        'visit_counter': 666,
    })
