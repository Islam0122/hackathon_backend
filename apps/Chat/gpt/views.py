from django.shortcuts import get_object_or_404
from rest_framework import permissions, status, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.Chat.Patient.models import Patient
from apps.Chat.gpt.models import ChatRequest as ChatRecord
from openai import OpenAI
from apps.Chat.gpt.serializers import *
from decouple import config

# from gtts import gTTS

client = OpenAI(api_key=config('GPT_SECRET_KEY'))


class GPTResponseApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = Messages

    def get(self, request, pk, *args, **kwargs):
        chat_records = ChatRecord.objects.filter(user=request.user, patient__id=pk)
        chat_records_serializer = ChatRecordSerializer(chat_records, many=True)
        return Response(chat_records_serializer.data, status=status.HTTP_200_OK)

    def post(self, request,pk, *args, **kwargs):
        serializer = Messages(data=request.data)

        if serializer.is_valid():
            input_text = serializer.validated_data['message']
            patient_instance = get_object_or_404(Patient, id=pk)

            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": "ты доктор, ты должен профессионально отвечать на вопросы пациентов. К тебе обращается пациент"
                                   "с болезнью, ты должен ему помочь и дать совет."
                    },
                    {
                        "role": "user",
                        "content": f"{input_text}",
                    }
                ],
                temperature=1,
            )

            chat_record = ChatRecord.objects.create(
                user=request.user,
                user_input=input_text,
                ai_response=response.choices[0].message.content,
                patient=patient_instance,
            )

            chat_record_serializer = ChatRecordSerializer(chat_record)

            response_data = {
                'message': response.choices[0].message.content,
                'chat_record': chat_record_serializer.data
            }

            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


