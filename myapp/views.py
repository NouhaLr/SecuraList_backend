from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from .models import DeviceSession, Product
from .serializers import DeviceSessionSerializer, ProductSerializer
from rest_framework.generics import ListAPIView


from .serializers import (
    RegisterSerializer,
    LoginSerializer,
    UserSerializer,
    ResetPasswordSerializer
)
User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'detail': 'Email ou mot de passe invalide.'}, status=401)

        if not user.check_password(password):
            return Response({'detail': 'Email ou mot de passe invalide.'}, status=401)

        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': UserSerializer(user).data
        })
    
class DashboadView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            'message': 'Bienvenue sur votre dashboard',
            'user': UserSerializer(user).data
        })

class ResetPasswordView(generics.GenericAPIView):
    serializer_class = ResetPasswordSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"detail": "Mot de passe réinitialisé avec succès."})
        return Response(serializer.errors, status=400)
    
class DeviceSessionCreateView(generics.CreateAPIView):
    serializer_class = DeviceSessionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        device_name = self.request.data.get("device_name")

        existing = DeviceSession.objects.filter(user=user, device_name=device_name).first()

        if existing:
            # On met à jour les infos
            existing.device_type = serializer.validated_data.get('device_type')
            existing.expires_at = serializer.validated_data.get('expires_at')
            existing.save()
        else:
            # On crée une nouvelle session
            serializer.save(user=user)
class DeviceSessionListView(generics.ListAPIView):
    serializer_class = DeviceSessionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return DeviceSession.objects.filter(user=self.request.user)
    
class MyDeviceSessionsView(generics.ListAPIView):
    serializer_class = DeviceSessionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return DeviceSession.objects.filter(user=self.request.user)
    
class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]
    def perform_create(self, serializer):
        
        serializer.save(user=self.request.user)

class ListProductsByCategoryView(ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        category = self.request.query_params.get('category', '')
        return Product.objects.filter(user=self.request.user, category__iexact=category)
    
class ProductListView(ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)