from django.urls import path,include
from . import views
from api.account.views import FacebookLogin

app_name = 'api'

urlpatterns = [
    path('', views.index ,name='index'),
    #path('', include('rest_framework.urls', namespace='rest_framework')),   
    path('account/', include('api.account.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('rest-auth/facebook/', FacebookLogin.as_view(), name='fb_login')

]