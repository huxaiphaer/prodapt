"""Views for endpoints."""
from rest_framework import generics, permissions, response, status
from rest_framework.views import APIView

from user import serializers


class LoginAPIView(generics.GenericAPIView):

    """Login APIView."""

    permission_classes = (permissions.AllowAny,)
    serializer_class = serializers.LoginSerializer

    def post(self, request, *args, **kwargs):
        """Add or create a user endpoint."""
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)


class RegisterAPIView(APIView):
    """"
    Register User APIView.
    """

    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.RegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={
            'request': request})
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data,
                                     status=status.HTTP_201_CREATED, )
        return response.Response(serializer.errors,
                                 status=status.HTTP_400_BAD_REQUEST)
