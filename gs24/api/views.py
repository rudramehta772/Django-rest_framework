from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import Mypermission
class StudentModelViewset(viewsets.ModelViewSet):
    queryset =  Student.objects.all()
    serializer_class = StudentSerializer