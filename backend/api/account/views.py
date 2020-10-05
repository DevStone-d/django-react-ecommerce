#Rest Framework
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,renderer_classes

#django
from django.contrib.auth.decorators import login_required

from account.models import Account

from rest_framework.authtoken.models import Token

from api.account.serializers import RegistrationSerializer


# Create your views here.

@api_view(['POST',])
@renderer_classes([JSONRenderer])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'Yeni kullanici basariyla kaydedildi.'
            data['email'] = account.email
            data['first_name'] = account.first_name
            data['last_name'] = account.last_name
            token = Token.objects.get(user=account).key
            data['token'] = token
        else :
            data = serializer.errors
        return Response(data)

@api_view(['GET',])
@renderer_classes([JSONRenderer])
def get_token(request):
    if request.method == 'GET':
        user = request.user
        token = Token.objects.get(user=account).key
        print(token)

