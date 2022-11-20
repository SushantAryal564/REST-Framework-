from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializers
from rest_framework import status
from rest_framework import viewsets

class StudentViewSet(viewsets.ViewSet):
  def list(self,request):
    print("**********List************")
    print("Basename:",self.basename)
    print("Actions:",self.action)
    print("Detail:",self.detail)
    print("Suffix:",self.suffix)
    print("Name:",self.name)
    print("Description: ",self.description)
    stu = Student.objects.all()
    serializer = StudentSerializers(stu,many=True)
    return Response(serializer.data)
  
  def retrieve(self,request,pk=None):
    print("**********Retrieve************")
    print("Basename:",self.basename)
    print("Actions:",self.action)
    print("Detail:",self.detail)
    print("Suffix:",self.suffix)
    print("Name:",self.name)
    print("Description: ",self.description)
    stu = Student.objects.get(pk=pk)
    serializer = StudentSerializers(stu)
    return Response(serializer.data)
    
  def create(self,request):
    print("**********create************")
    print("Basename:",self.basename)
    print("Actions:",self.action)
    print("Detail:",self.detail)
    print("Suffix:",self.suffix)
    print("Name:",self.name)
    print("Description: ",self.description)
    serializer = StudentSerializers(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({'msg':'Data Created'},status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def update(self,request,pk=None):
    print("**********Update************")
    print("Basename:",self.basename)
    print("Actions:",self.action)
    print("Detail:",self.detail)
    print("Suffix:",self.suffix)
    print("Name:",self.name)
    print("Description: ",self.description)
    stu = Student.objects.get(pk=pk)
    serializer = StudentSerializers(stu, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({'msg':'Complete Data Update'})
    return Response(serializer.errors)
  
  def partial_update(self,request,pk):
    print("**********Partial Update************")
    print("Basename:",self.basename)
    print("Actions:",self.action)
    print("Detail:",self.detail)
    print("Suffix:",self.suffix)
    print("Name:",self.name)
    print("Description: ",self.description)
    stu = Student.objects.get(pk=pk)
    serializer = StudentSerializers(stu, data=request.data,partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response({'msg':'Complete Data Update'})
    return Response(serializer.errors)
  
  def destroy(self,request,pk):
    print("**********Destroy************")
    print("Basename:",self.basename)
    print("Actions:",self.action)
    print("Detail:",self.detail)
    print("Suffix:",self.suffix)
    print("Name:",self.name)
    print("Description: ",self.description)
    stu = Student.objects.get(pk=pk)
    stu.delete()
    return Response({'msg':'Data Deleted'})


