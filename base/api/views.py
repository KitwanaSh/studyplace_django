from django.http import JsonResponse

def getResponse(request):
    responses = [
        "GET /api",
        "GET /api/rooms",
        "GET /api/rooms/:id"
    ]

    return JsonResponse(responses, safe=False)