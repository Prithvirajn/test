from django.test import TestCase
from .chatbot_model import get_chatbot_response, initialize_chatbot

class ChatbotTestCase(TestCase):
    def setUp(self):
        # Initialize the chatbot before running each test
        self.chatbot = initialize_chatbot()

    def test_chatbot_response(self):
        # Simulate a user input
        user_input = "Hello"
        
        # Get the response from the chatbot
        response = get_chatbot_response(user_input, self.chatbot)
        
        # Assert that the response contains the word "Hello" (or similar logic)
        self.assertIn("Hello", response, f"Expected response to contain 'Hello', but got: {response}")
        
    def test_empty_input(self):
        # Test case where the user input is empty
        user_input = ""
        
        # Get the response from the chatbot
        response = get_chatbot_response(user_input, self.chatbot)
        
        # Check if response is not empty (chatbot should always respond)
        self.assertGreater(len(response), 0, "Response should not be empty")
    
    def test_bot_answer(self):
        # Test case to check for specific response content
        user_input = "What is your name?"
        
        # Get the response from the chatbot
        response = get_chatbot_response(user_input, self.chatbot)
        
        # Check if the response contains an expected phrase (e.g., "I am a bot")
        self.assertIn("I am a bot", response, f"Expected response to contain 'I am a bot', but got: {response}")

    def test_response_length(self):
        # Test case to check that the response length doesn't exceed a limit
        user_input = "Tell me a joke!"
        
        # Get the response from the chatbot
        response = get_chatbot_response(user_input, self.chatbot)
        
        # Check if the response length is within an acceptable range (e.g., less than 150 characters)
        self.assertLess(len(response), 150, "Response is too long")
