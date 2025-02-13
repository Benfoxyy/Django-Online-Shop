from rest_framework.generics import GenericAPIView
from .serializers import SignUpApiSerializers
from rest_framework.response import Response
from rest_framework import status


class SignUpApiView(GenericAPIView):
    serializer_class = SignUpApiSerializers

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {
            "datail": "User registered successfully",
        }
        return Response(data, status=status.HTTP_201_CREATED)
