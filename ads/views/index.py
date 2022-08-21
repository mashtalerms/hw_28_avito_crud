from django.http import JsonResponse


def index(request):
    """Root view"""
    return JsonResponse({"status": "ok"}, status=200)