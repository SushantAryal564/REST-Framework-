import requests
import json

URL ="http://127.0.0.1:8000/studentapi/"

def get_data(id = None):
  data = {}
  if id is not None:
    data ={"id":id}
  json_data = json.dumps(data)
  r = requests.get(url=URL,data=json_data)
  # data = json.load(r)
  print(r.json())
    
# get_data()

def post_data():
  data={
    "name":"Rokchaya Dhungana",
    "roll":170,
    "city":'kathmandu'
  }
  json_data = json.dumps(data)
  r = requests.post(url=URL,data=json_data)
  print(r.json())
  
# post_data()

def update_data():
  data={
    "id":"4",
    "name":"Rashmi Dhungana",
    "city":'Syangja'
  }
  json_data = json.dumps(data)
  r = requests.put(url=URL,data=json_data)
  print(r.json())
  
# update_data();

def delete_data():
  data={
    "id":"3",
  }
  json_data = json.dumps(data)
  r = requests.delete(url=URL,data=json_data)
  print(r.json())
  
delete_data();