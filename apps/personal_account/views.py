from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Doctor
from .serializers import DoctorSerializer
from rest_framework import status


class DoctorProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        doctor = Doctor.objects.get(user=request.user)
        serializer = DoctorSerializer(doctor)
        return Response(serializer.data)

    def put(self, request):
        doctor = Doctor.objects.get(user=request.user)
        serializer = DoctorSerializer(doctor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)