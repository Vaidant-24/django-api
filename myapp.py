import requests
import json

URL = 'http://127.0.0.1:8000/student_api/'

# def post_data():
#     data = {
#     'name': 'Sunny',
#     'roll': '30',
#     'city': 'Rajkot'}
#     headers = {'Content-Type': 'application/json'}
#     json_data = json.dumps(data)
#     r = requests.post(url = URL,headers=headers, data=json_data)
#     data = r.json()
#     print(data)

# post_data()

# def get_data(id = None):
#     data = {}
#     if id is not None:
#         data = { 'id': id }
#     json_data = json.dumps(data)
#     headers = { 'Content-Type': 'application/json' }
#     r = requests.get(url=URL,headers=headers, data=json_data)
#     data = r.json()
#     print(data)

# get_data()


# URL = 'http://127.0.0.1:8000/stuupdate/'

# def update_data():
#     data = {
#     'id': 3,
#     'name': 'Shushant',
#     'city': 'Barwaha'}
#     headers = {'Content-Type': 'application/json'}
#     json_data = json.dumps(data)
#     r = requests.put(url = URL,headers=headers ,data=json_data )
#     data = r.json()
#     print(data)

# update_data()

# URL = 'http://127.0.0.1:8000/studelete/'

def delete_data():
    data = {'id' : 4}
    headers = {'Content-Type': 'application/json'}
    json_data = json.dumps(data)
    r = requests.delete(url = URL,headers=headers, data = json_data)
    data = r.json()
    print(data)

delete_data()