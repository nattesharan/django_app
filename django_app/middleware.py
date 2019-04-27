'''
A middleware is something whichis called between the request and response cycle.
Middleware class should define at least one of the following methods:
Called during request:
    1)process_request(request)
    2)process_view(request, view_func, view_args, view_kwargs)
Called during response:
    1)process_exception(request, exception) (only if the view raised an exception)
    2)process_template_response(request, response) (only for template responses)
    3)process_response(request, response)
The Middlware classes are called twice during the request/response life cycle. For that reason, 
the order you define the Middlwares in the MIDDLEWARE_CLASSES configuration is important.
During the request cycle, the Middleware classes are executed top-down.For each of the Middlewares it will 
execute the process_request() and process_view() methods.At this point, Django will do all the work on your view function.
After the work is done (e.g. querying the database, paginating results, processing information, etc), it will return 
a response for the client.
During the response cycle, the Middleware classes are executed bottom-up.For each of the 
Middlewares it will execute the process_exception(), process_template_response() and process_response() methods.
'''
import re
from django.shortcuts import redirect
from django.conf import settings

EXEMPT_URLS = [re.compile(settings.LOGIN_URL.lstrip('/'))]
EXEMPT_URLS += [re.compile(url) for url in settings.LOGIN_EXEMPT_URLS]
class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        response = self.get_response(request)
        return response
    
    def process_view(self, request, view_func, view_args, view_kwargs):
        assert hasattr(request, 'user')
        path = request.path_info.lstrip('/')
        if 'api' in path:
            return None
        is_exempt_url = any(url.match(path) for url in EXEMPT_URLS)
        if request.user.is_authenticated() and is_exempt_url:
            return redirect(settings.LOGIN_REDIRECT_URL)
        elif not request.user.is_authenticated() and not is_exempt_url:
            return redirect(settings.LOGIN_URL)
        else:
            return None
