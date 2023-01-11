from django.shortcuts import render
from .models import Student
from .serializers import Studentselerilizer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse


# Create your views here.

#model object - Single Student Data
def student_detail(request, pk):
    stu = Student.objects.get(id = pk)
    #print(stu,'stu')
    serializer = Studentselerilizer(stu)
    #print(serializer,'serializer')
    #print(serializer.data,'serilalizer.data')
    #sjson_data = JSONRenderer().render(serializer.data)
    #print(json_data,'json_data')
    #return HttpResponse(json_data, content_type = 'application/json')
    return JsonResponse(serializer.data, safe=False)


#query set - All Student Data
def student_list(request):
    stu = Student.objects.all()
    #print(stu,'stu')
    serializer = Studentselerilizer(stu, many=True)
    #print(serializer,'serializer')
    #print(serializer.data,'serilalizer.data')
    #json_data = JSONRenderer().render(serializer.data)
    #print(json_data,'json_data')
    #return HttpResponse(json_data, content_type = 'application/json')
    return JsonResponse(serializer.data, safe=False)