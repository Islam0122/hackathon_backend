from rest_framework import serializers
from apps.Chat.gpt.models import ChatRequest as ChatRecord


class Messages(serializers.Serializer):
    message = serializers.CharField(write_only=True)


class ChatRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRecord
        fields = ('patient', 'user_input', 'ai_response', 'timestamp', 'user')


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRecord
        fields = '__all__'
