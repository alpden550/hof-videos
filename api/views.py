import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from halls.models import Hall
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from django.views.decorators.http import require_http_methods


@csrf_exempt
@require_http_methods(['DELETE'])
def delete_hall(request):
    """Simple endpoint to delete hall."""
    hall_id = json.loads(request.body).get('hall_id')
    hall = get_object_or_404(Hall, pk=hall_id)
    if not hall.user == request.user:
        raise PermissionDenied

    hall.delete()
    return JsonResponse(status=204, data={'message': 'Deleted successful', 'status': 204})


@csrf_exempt
@require_http_methods(['POST'])
def update_hall(request):
    """Endpoint to edit hall title."""
    json_data = json.loads(request.body)
    hall = get_object_or_404(Hall, pk=json_data.get('hall_id'))
    if not hall.user == request.user:
        raise PermissionDenied

    hall.title = json_data.get('text')
    hall.save()
    return JsonResponse({'message': 'Deleted successful', 'status': 200})
