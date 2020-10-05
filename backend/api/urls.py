from django.urls import path,include
from . import views

app_name = 'api'

urlpatterns = [
    path('', views.index ,name='index'),
    #path('', include('rest_framework.urls', namespace='rest_framework')),   
    path('account/', include('api.account.urls')),
    path('products/', include('api.products.urls')),
    path('collections/', include('api.collections.urls')),
]