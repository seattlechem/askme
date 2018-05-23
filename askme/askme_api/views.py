"""Rest Api views."""
from rest_framework.views import APIView
from rest_framework.response import Response
from .rectotext import rec_to_text
from .search import find
from django.http import HttpResponse
from gtts import gTTS
import os

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


class AudioViewApi(APIView):
    """Using apiview."""

    def post(self, request):
        """Upload audio file."""
        uploadedFile = open("askme/assets/file.wav", "wb")
        f = request.FILES['data']
        uploadedFile.write(f.read())
        uploadedFile.close()
        question = rec_to_text()
        answer = find(question)
        tts = gTTS(text=answer, lang='en')
        tts.save("askme/assets/good.mp3")
        # os.system("mpg321 good.mp3")
        fname = "askme/assets/good.mp3"
        f = open(fname, "rb") 
        response = HttpResponse()
        response.write(f.read())
        response['Content-Type'] = 'audio/mp3'
        response['Content-Length'] = os.path.getsize(fname)
        return response

