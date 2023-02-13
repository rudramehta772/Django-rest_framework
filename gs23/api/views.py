from .models import Student
from django.shortcuts import render
from rest_framework.response import Response
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly
from .permissions import Mypermission
from rest_framework import status

def student_api(request, pk=None):
    if request.method == 'GET':
        id = pk
        if id is not None:
            stu = Student.objects.get(id = id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        
        stu = Student.objects.all()
        serializer = StudentSerializer(stu)

""" class StudentModelViewset(viewsets.ModelViewSet):
    queryset =  Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes =[SessionAuthentication]
    #permission_classes = [AllowAny]
    #permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    permission_classes = [Mypermission] """