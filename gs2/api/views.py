from django.shortcuts import render
import io
from .serializers import StudentSerializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def student_create(request):
  if request.method == "POST":
    json_data = request.body
    stream = io.BytesIO(json_data)
    pythondata = JSONParser().parse(stream)
    serializer = StudentSerializers(data = pythondata)
    if serializer.is_valid():
      serializer.save()
      res={'msg':'Data created'}
      json_data = JSONRenderer().render(res);
      print("I am json data ",json_data)
      return JsonResponse(json_data)
    json_data = JSONRenderer().render(serializer.errors)
    return JsonResponse(json_data)
    
    