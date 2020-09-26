import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from halls.models import Hall
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied


@csrf_exempt
def delete_hall(request):
    """Simple endpoint to delete hall."""
    hall_id = json.loads(request.body).get('hall_id')
    hall = get_object_or_404(Hall, pk=hall_id)
    if not hall.user == request.user:
        raise PermissionDenied

    if request.method == 'DELETE':
        hall.delete()
        return JsonResponse(status=204, data={'message': 'Deleted successful', 'status': 204})
    else:
        return JsonResponse(status=405, data={'message': 'Method not allowed', 'status': 405})
