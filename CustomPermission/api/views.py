from .models import Student
from .serializers import StudentSerializers
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly
from .custompermissions import MyPermission
class StudentReadOnlyModelViewSet(viewsets.ModelViewSet):
  queryset = Student.objects.all()
  serializer_class = StudentSerializers
  authentication_classes =[SessionAuthentication]
  permission_classes = [MyPermission]

