from django.shortcuts import render
from django.http import HttpResponse
from .rectotext import rec_to_text
from askme_api.search import find
from django.views.decorators.csrf import csrf_exempt
from gtts import gTTS
import os


def home_view(request):
    """
    The home_view function opens the recorded file in the file structure
    and writes it as the request.body and then the audio gets set as text
    and answered by the find() method
    """
    return render(request, 'generic/base.html')


@csrf_exempt
def save_view(request):
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
