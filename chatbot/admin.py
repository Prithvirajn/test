from django.contrib import admin
from .models import ChatHistory  # If you have a model like ChatHistory

# Register your models here.
# For example, if you have a model called ChatHistory:

@admin.register(ChatHistory)
class ChatHistoryAdmin(admin.ModelAdmin):
    list_display = ('user_message', 'bot_response', 'timestamp')  # Display relevant fields
    search_fields = ('user_message', 'bot_response')  # Allow search by message content
    list_filter = ('timestamp',)  # Filter by timestamp
