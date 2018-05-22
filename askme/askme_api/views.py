"""Rest Api views."""
from rest_framework.views import APIView
from rest_framework.response import Response


class AskViewApi(APIView):
    """Using apiview."""

    def get(self, request):
        """Get request."""
        return Response()

    def post(self, request):
        """Upload audio file."""

        customHeader = request.META['HTTP_MYCUSTOMHEADER']
        uploadedFile = open("file.wav", "wb")
        uploadedFile.write(request.body)
        uploadedFile.close()
        return HttpResponse(escape(repr(request)))
