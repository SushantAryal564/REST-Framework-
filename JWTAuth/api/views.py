from .models import Student
from .serializers import StudentSerializers
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from api.customauth import CustomAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
class StudentRModelViewSet(viewsets.ModelViewSet):
  queryset = Student.objects.all()
  serializer_class = StudentSerializers
  authentication_classes = [JWTAuthentication]
  permission_classes = [IsAuthenticated]
  


