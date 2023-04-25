from django.shortcuts import render, redirect
from home.models import *
from django.contrib.auth.decorators import login_required
import openai
import os
import dotenv
from django.contrib import messages

dotenv.load_dotenv()
openai.api_key = os.getenv('API_KEY')

@login_required(login_url='home')
def index(request):
    categories = Category.objects.all()

    sideBar = ""
    topics = Topic.objects.all()

    return render(request, 'chatIndex.html', {"categories": categories, "sidebar": sideBar, 'topics': topics})

def sendQuestion(request):

    categories = Category.objects.all()
    topics = Topic.objects.all()
    
    try:
        if request.method == 'POST':
            prompt = request.POST.get('prompt')
            history = {}
            if  request.POST.get('history'):
                history = eval(request.POST.get('history'))

            response = openai.Completion.create(model="text-davinci-003", prompt=prompt, temperature=1, max_tokens=1000)
            formatted_response = response['choices'][0]['text']

            history[str(getLastIndex(history) + 1)] = {"prompt":prompt, "response": str(formatted_response)}

            context = {
                'formatted_response': formatted_response,
                'prompt': prompt,
                "categories": categories,
                'topics': topics,
                'history': history
            }
            # this will render the results in the home.html template
            return render(request, 'chatIndex.html', context)
    except Exception as err:
        #messages.warning(request, request.POST.get('history'))
        history[str(getLastIndex(history) + 1)] = {"prompt":prompt, "response": str(err)}

        context = {
            'prompt': prompt,
            "categories": categories,
            'topics': topics,
            'history': history
        }
        return render(request, 'chatIndex.html', context)
        pass
        
    return render(request, 'chatIndex.html', {"categories": categories, 'topics': topics})


def getLastIndex(dictionaryFile):
    if len(dictionaryFile) > 0 :
        return int(list(dictionaryFile)[-1])
    else:
        return -1