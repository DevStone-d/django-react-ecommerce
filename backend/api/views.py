from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication,BasicAuthentication

##Serializer Class
from api.account.serializers import AccountDetailSerializer
# Create your views here.

@api_view(['GET',])
def index(request):
    return Response(status=status.HTTP_404_NOT_FOUND)

