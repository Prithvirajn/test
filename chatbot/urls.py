from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat, name='chat'),
    path('get-response/', views.chatbot_response, name='chatbot_response'),
]
