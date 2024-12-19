from django.http import JsonResponse
from django.shortcuts import render
from .chatbot_model import ChatbotModel

# Load the chatbot model
chatbot = ChatbotModel()

def chat(request):
    return render(request, 'chatbot/chat.html')

def chatbot_response(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input', '')
        response = chatbot.get_response(user_input)
        return JsonResponse({'response': response})
    return JsonResponse({'error': 'Invalid request'}, status=400)
