from rest_framework.views import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from django.shortcuts import get_object_or_404
from core.serializers import UserSerializer
from core.models import User

@permission_classes([IsAuthenticated])
class ProfileViewSet(ViewSet):
    def retrieve(self, request):
        try:
            user = request.user
            ser = UserSerializer(instance=user)
            return Response(ser.data)
        except User.DoesNotExist:
            return Response(status=404)
    
    def update(self, request):
        user = request.user
        ser = UserSerializer(data=request.data)
        if ser.is_valid():
            user = ser.update(user, ser.validated_data)
            return Response(status=200)
        else:
            return Response(ser.errors, status=400)
    
    def remove_account(self, request):
        request.user.delete()
        return Response(status=200)
