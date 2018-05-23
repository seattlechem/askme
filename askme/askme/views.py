
from django.shortcuts import render
from askme_api.rectotext import rec_to_text
from askme_api.search import find


def home_view(request):
    """
    The home_view function opens the recorded file in the file structure
    and writes it as the request.body and then the audio gets set as text
    and answered by the find() method
    """
    uploadedFile = open("file.wav", "wb")
    uploadedFile.write(request.body)
    uploadedFile.close()
    question = rec_to_text()
    answer = find(question)
    return render(request, 'generic/base.html', {'message': answer})
