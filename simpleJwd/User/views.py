from django.shortcuts import render
from rest_framework.response import Response
from User.serializers import CustomTokenObtainPairSerializer
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view(['post'])
@permission_classes([IsAuthenticated])
def login_view(request):
    serializer = CustomTokenObtainPairSerializer(data=request.data)
    try:
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data)
    except Exception as e:
        return Response({'detail':str(e)})
    

# Create your views here.
