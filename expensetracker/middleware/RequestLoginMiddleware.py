from tracker.models import RequestLogs

class RequestLogin:
    def __init__(self, get_response) -> None:
        self.get_response = get_response

    def __call__(self, request):
        # Log request details (example implementation)
        try:
            RequestLogs.objects.create(
                request_info=vars(request),
                request_type=request.method,
                request_path=request.path,  # Example additional field
            )
        except Exception as e:
            # Handle errors, such as database issues
            print(f"Error logging request: {e}")

        # Process the request and get the response
        response = self.get_response(request)

        return response
