from rest_framework import serializers
from .models import Student

def start_with_r(value):
  if value[0].lower() != "r":
    raise serializers.ValidationError('Name should start with R')

class StudentSerializers(serializers.ModelSerializer):
  # name = serializers.CharField(read_only = True)
  name = serializers.CharField(validators=[start_with_r])
  class Meta:
    model= Student
    fields= ['name','roll','city']
    # read_only_fields = ['name','roll']
    # extra_kwargs = {'name':{'read_only':True}}
  
  #Field Level Validation
  # def validate_roll(self,value):
  #   if value >= 200:
  #     raise serializers.ValidationError('Seat Full')
  #   return value
  
  # Object Level Valiation
  # def validate(self,data):
  #   nm = data.get('name')
  #   ct = data.get('city')
  #   if str(nm).lower() == 'sushant' and str(ct).lower() != 'kathmandu':
  #     raise serializers.ValidationError("City must be Kathmandu")
  #   return data
  
    
  