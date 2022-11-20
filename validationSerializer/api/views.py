from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.utils.decorators import method_decorator
# Class based View
@method_decorator(csrf_exempt,name='dispatch')
class StudentAPI(View):
  def get(self,request,*args,**kwargs):
    json_data = request.body
    stream = io.BytesIO(json_data)
    pythondata = JSONParser().parse(stream)
    id = pythondata.get('id',None)
    if id is not None:
      stu = Student.objects.get(id = id)
      serializers = StudentSerializers(stu)
      json_data = JSONRenderer().render(serializers.data)
      return HttpResponse(json_data,content_type = "application/json")
      # return JsonResponse(serializers.data)
    stu = Student.objects.all()
    serializers = StudentSerializers(stu,many=True)
    json_data = JSONRenderer().render(serializers.data)
    return HttpResponse(json_data,content_type = "application/json")
    # return JsonResponse(serializers.data,safe=False)
  
  def post(self,request,*args,**kwargs):
    json_data = request.body
    stream = io.BytesIO(json_data)
    pythondata = JSONParser().parse(stream)
    serializers = StudentSerializers(data = pythondata)
    if serializers.is_valid():
      serializers.save()
      res = {'msg':'Data Created'}
      return JsonResponse(res)
    return JsonResponse(serializers.errors)
  
  def put(self,request,*args,**kwargs):
    json_data = request.body
    stream = io.BytesIO(json_data)
    pythondata = JSONParser().parse(stream)
    id = pythondata.get('id')
    stu = Student.objects.get(id = id)
    # To update all data
    serializers = StudentSerializers(stu,data = pythondata)
    # Partial Update
    # serializers = StudentSerializers(stu, data=pythondata,partial=True)
    if serializers.is_valid():
      serializers.save()
      res = {'msg':'Data updated'}
      return JsonResponse(res)
    return JsonResponse(serializers.errors)
  
  def delete(self,request,*args,**kwargs):
    json_data =  request.body
    stream = io.BytesIO(json_data)
    pythondata = JSONParser().parse(stream)
    id = pythondata.get('id')
    stu = Student.objects.get(id=id)
    stu.delete();
    res = {"msg":"Successfully data deleted"}
    return JsonResponse(res,safe=False)
    
# Function based View
@csrf_exempt
def student_api(request):
  if request.method == "GET":
    json_data = request.body
    stream = io.BytesIO(json_data)
    pythondata = JSONParser().parse(stream)
    id = pythondata.get('id',None)
    if id is not None:
      stu = Student.objects.get(id = id)
      serializers = StudentSerializers(stu)
      json_data = JSONRenderer().render(serializers.data)
      return HttpResponse(json_data,content_type = "application/json")
      # return JsonResponse(serializers.data)

    stu = Student.objects.all()
    serializers = StudentSerializers(stu,many=True)
    json_data = JSONRenderer().render(serializers.data)
    return HttpResponse(json_data,content_type = "application/json")
    # return JsonResponse(serializers.data,safe=False)
  
  if request.method == "POST":
    json_data = request.body
    stream = io.BytesIO(json_data)
    pythondata = JSONParser().parse(stream)
    serializers = StudentSerializers(data = pythondata)
    if serializers.is_valid():
      serializers.save()
      res = {'msg':'Data Created'}
      return JsonResponse(res)
    return JsonResponse(serializers.errors)
  
  if request.method == "PUT":
    json_data = request.body
    stream = io.BytesIO(json_data)
    pythondata = JSONParser().parse(stream)
    id = pythondata.get('id')
    stu = Student.objects.get(id = id)
    # To update all data
    serializers = StudentSerializers(stu,data = pythondata)
    # Partial Update
    # serializers = StudentSerializers(stu, data=pythondata,partial=True)
    if serializers.is_valid():
      serializers.save()
      res = {'msg':'Data updated'}
      return JsonResponse(res)
    return JsonResponse(serializers.errors)
  
  if request.method == "DELETE":
    json_data =  request.body
    stream = io.BytesIO(json_data)
    pythondata = JSONParser().parse(stream)
    id = pythondata.get('id')
    stu = Student.objects.get(id=id)
    stu.delete();
    res = {"msg":"Successfully data deleted"}
    return JsonResponse(res,safe=False)

    
    
  
  
    
  
  
      