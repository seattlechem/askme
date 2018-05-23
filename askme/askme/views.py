from django.shortcuts import render
from askme_api.rectotext import rec_to_text
from askme_api.search import find
from django.views.decorators.csrf import csrf_exempt



def home_view(request):
    """
    The home_view function opens the recorded file in the file structure
    and writes it as the request.body and then the audio gets set as text
    and answered by the find() method
    """
    return render(request, 'generic/base.html')


@csrf_exempt
def save_view(request):
    import pdb; pdb.set_trace()
    uploadedFile = open("askme/assets/file.wav", "wb")
    f = request.FILES['data']
    uploadedFile.write(f.read())
    uploadedFile.close()
    question = rec_to_text()
    answer = find(question)
    print(answer)
    return {answer}
    
