"""Rest Api views."""
from rest_framework.views import APIView
from rest_framework.response import Response
from .rectotext import rec_to_text
from .search import find


class AskViewApi(APIView):
    """Using apiview."""

    def post(self, request):
        """Upload audio file."""
        uploadedFile = open("askme_api/assets/file.wav", "wb")
        # import pdb; pdb.set_trace()
        f = request.FILES['file']
        uploadedFile.write(f.read())
        uploadedFile.close()
        question = rec_to_text()
        answer = find(question)
        import pdb; pdb.set_trace()
        return {'answer': answer}
