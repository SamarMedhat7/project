from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from .serializers import RegisterSerializer, UserSerializer
from .models import CustomUser

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

class LoginView(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            return Response({'message': 'Login successful', 'user': UserSerializer(user).data}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class StudentDashboardView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        if request.user.user_type != 'student':
            return Response({'error': 'You do not have permission to access this page.'},
                            status=status.HTTP_403_FORBIDDEN)
        return Response({'message': 'student dashboard data!'})

class AdminDashboardView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        if request.user.user_type != 'admin':
            return Response({'error': 'You do not have permission to access this page.'},
                            status=status.HTTP_403_FORBIDDEN)
        return Response({'message': 'admin dashboard data!'})

class TeacherDashboardView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        if request.user.user_type != 'teacher':
            return Response({'error': 'You do not have permission to access this page.'},
                            status=status.HTTP_403_FORBIDDEN)
        return Response({'message': 'teacher dashboard data!'})
