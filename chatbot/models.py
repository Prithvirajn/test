from django.db import models

class ChatHistory(models.Model):
    user_message = models.TextField()
    bot_response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Chat {self.id} - {self.timestamp}"

    class Meta:
        ordering = ['-timestamp']  # Orders chats from the most recent
