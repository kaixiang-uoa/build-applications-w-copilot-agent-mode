from django.http import JsonResponse

def api_root(request):
    return JsonResponse({
        "message": "Welcome to the OctoFit API!",
        "codespace_url": "https://improved-goggles-9p966pxv4xvh7qj6-8000.app.github.dev",
        "localhost_url": "http://localhost:8000"
    })