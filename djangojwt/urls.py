"""
URL configuration for djangojwt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
#from myapp.views import RegisterView,LoginView,DashboadView,ResetPasswordView
from myapp.views import *
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from myapp.views import ListProductsByCategoryView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/register/',RegisterView.as_view(),name="auth_register"),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/auth/login/',LoginView.as_view(),name="auth_login"),
    path('api/dashboard/',DashboadView.as_view(),name="dashboard"),
    path('api/auth/reset-password/', ResetPasswordView.as_view(), name='reset_password'),
    path('api/devices/create/', DeviceSessionCreateView.as_view(), name='create_device'),
    path('api/devices/mine/', DeviceSessionListView.as_view(), name='my_devices'),
    path('devices/mine/', MyDeviceSessionsView.as_view(), name='my-device-sessions'),
    path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path('products/create/', ProductCreateView.as_view(), name='create-product'),
     path('products/by-category/', ListProductsByCategoryView.as_view(), name='products-by-category'),
     path('products/', ProductListView.as_view(), name='product-list'),

]
