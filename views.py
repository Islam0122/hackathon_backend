import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from drf_yasg.utils import swagger_auto_schema
from .serializers import *

logger = logging.getLogger(__name__)


class RegistrationView(APIView):

    @swagger_auto_schema(request_body=RegistrationSerializer)
    def post(self, request):
        try:
            serializer = RegistrationSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response('Account has been successfully created', status=201)
        except Exception as e:
            logger.error(f'An error occurred: {e}')
            return Response('An error occurred during registration', status=500)


class ActivationView(APIView):

    @swagger_auto_schema(request_body=ActivationSerializer)
    def post(self, request):
        try:
            serializer = ActivationSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.activate()
            return Response('User has been activated', status=200)
        except Exception as e:
            logger.error(f'An error occurred: {e}')
            return Response('An error occurred during activation', status=500)


class LoginView(ObtainAuthToken):
    serializer_class = LoginSerializer


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        try:
            user = request.user
            Token.objects.filter(user=user).delete()
            return Response('You have successfully logged out')
        except Exception as e:
            logger.error(f'An error occurred: {e}')
            return Response('An error occurred during logout', status=500)

