from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializers

@api_view(['GET','POST','PUT','DELETE','PATCH'])
def student_api(request, pk = None):
  if request.method == "GET":
    id = pk
    if id is not None:
      stu = Student.objects.get(pk=id)
      serializer = StudentSerializers(stu)
      return Response(serializer.data)
    stu = Student.objects.all()
    serializer = StudentSerializers(stu,many=True)
    return Response(serializer.data)
  
  if request.method == "POST":
    serializer = StudentSerializers(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({'msg':'Data Created'})
    return Response(serializer.errors)
  
  if request.method == "PUT":
    id = pk
    stu = Student.objects.get(pk = id)
    serializer = StudentSerializers(stu,data=request.data,partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response({'msg':'complete data updated'})
    return Response(serializer.errors)
  
  if request.method == "PATCH":
    id = pk
    stu = Student.objects.get(pk=id)
    serializer = StudentSerializers(stu,data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({'msg':'partial data updated'})
    return Response(serializer.errors)
  
  if request.method == "DELETE":
    id = pk
    stu = Student.objects.get(pk=id)
    stu.delete()
    return Response({'msg':'Data deleted Successfully'})
  
