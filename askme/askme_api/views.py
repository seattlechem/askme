"""Rest Api views."""
from rest_framework.views import APIView
from rest_framework.response import Response
from .rectotext import rec_to_text
from .search import find
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from gtts import gTTS
import os
from askme.settings import BASE_DIR

@method_decorator(csrf_exempt, name='dispatch')
class AskViewApi(APIView):
    """Using apiview."""

    def post(self, request):
        """Upload audio file."""
        try:
            f = request.FILES['file']
            uploadedFile = open(os.path.join(BASE_DIR, "askme_api/assets/file.wav", "wb"))
            uploadedFile.write(f.read())
            uploadedFile.close()
            question = rec_to_text()
            answer = find(question)
        except KeyError:
            answer = "Sorry we have some connection problems.\
 I didn't catch your request"
        return JsonResponse({'answer': answer})


@method_decorator(csrf_exempt, name='dispatch')
class AudioViewApi(APIView):
    """Using apiview."""

    def post(self, request):
        """Upload audio file."""
        try:
            uploadedFile = open(os.path.join(BASE_DIR, 'askme/assets/file.wav'), 'wb')
            f = request.FILES['data']
            uploadedFile.write(f.read())
            uploadedFile.close()
            question = rec_to_text()
            answer = find(question)
        except KeyError:
            answer = 'I am sorry. We have some connection issues.\
I couldn\'t get get Your file'

        tts = gTTS(text=answer, lang='en')
        fname = os.path.join(BASE_DIR, "askme/assets/good.mp3")
        tts.save(fname)
        f = open(fname, "rb") 
        response = HttpResponse()
        response.write(f.read())
        response['Content-Type'] = 'audio/mp3'
        response['Content-Length'] = os.path.getsize(fname)
        return response
