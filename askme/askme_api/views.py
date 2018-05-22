"""Rest Api views."""
from rest_framework.views import APIView
from rest_framework.response import Response
from .rectotext import rec_to_text
from .search import find


class AskViewApi(APIView):
    """Using apiview."""

    def get(self, request):
        """Get request."""
        return Response()

    def post(self, request):
        """Upload audio file."""
        uploadedFile = open("file.wav", "wb")
        uploadedFile.write(request.body)
        uploadedFile.close()
        question = rec_to_text()
        answer = find(question)
        return {'answer': answer}
