from django.http import StreamingHttpResponse
from rest_framework.views import APIView
from django.conf import settings


class LogView(APIView):
    def get(self, request):
        # Get the logger instance
        file = settings.LOGGING['handlers']['file']['filename']

        def log_generator():
            # Open the log file
            with open(file, 'r') as f:
                logs = f.readlines()
                # Read the logs from the file
                for line in logs[-1000:]:
                    yield line
        # Return the logs as a streaming response
        return StreamingHttpResponse(log_generator(), content_type='text/plain')
