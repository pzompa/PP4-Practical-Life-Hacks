from django.urls import resolve
import logging

logger = logging.getLogger(__name__)

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Log session information
        session_data = dict(request.session)
        logger.info("Session data:")
        for key, value in session_data.items():
            logger.info(f"{key}: {value}")

        response = self.get_response(request)

        match = resolve(request.path_info)
        url_name = match.url_name

        view_func = match.func
        if hasattr(view_func, '__name__'):
            view_name = view_func.__name__
        else:
            view_name = view_func.__class__.__name__

        logger.info(f"Request path: {request.path}, URL pattern name: {url_name}, View class: {view_name}")

        return response
