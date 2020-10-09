from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView

class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter

@api_view(['GET',])
def index(request):
    return Response(status=status.HTTP_404_NOT_FOUND)