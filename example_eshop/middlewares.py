from django.http import HttpResponse

from apps.credentials.models import Credentials


class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        if not any(x in request.path for x in ['admin', 'docs']):
            token = request.headers.get('X-Token')
            if not token:
                return HttpResponse(status=401)

            credentials = Credentials.objects.filter(token=token).first()
            if not credentials:
                return HttpResponse(status=401)

            request.token = credentials.example_token

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
