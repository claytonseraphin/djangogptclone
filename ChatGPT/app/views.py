from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import openai
import os

openai.api_key = "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"


# Create your views here.

def index(request):
    return render(request, 'app/index.html')


@csrf_exempt
def get_bot_response(request):
    answer = ''
    if request.method == "POST":
        userText = request.POST.get('msg')
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=userText,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=1
        )
        print(response)
        answer = response["choices"][0]["text"]
        print(answer)
        return JsonResponse({'answer': answer})
    return render(request, 'app/index.html', {'answer': answer})
