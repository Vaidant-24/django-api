import io
from django.shortcuts import render
from api.models import Student
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from api.serializers import StudentSerializer
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializers = StudentSerializer(data = pythondata)
        if serializers.is_valid():
            serializers.save()
            res  = {'msg': 'data saved successfully'}
            json_data = JSONRenderer().render(res)
            return  HttpResponse(json_data , content_type='application/json')
        json_data = JSONRenderer().render(serializers.errors)
        return HttpResponse(json_data , content_type='application/json')    
    
def student_detail(request):
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        if id is not None:
            stu = Student.objects.get(id=id)
            serializers = StudentSerializer(stu)
            json_data = JSONRenderer().render(serializers.data)
            return HttpResponse(json_data,content_type='application/json')
        stu = Student.objects.all()
        serializers = StudentSerializer(stu , many = True)
        json_data = JSONRenderer().render(serializers.data)
        return HttpResponse(json_data,content_type='application/json')
@csrf_exempt      
def student_update(request):
    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        serialzers = StudentSerializer(stu ,data = pythondata , partial = True)
        if serialzers.is_valid():
            serialzers.save()
            res = {'msg': 'data updated successfully'}
            json_data= JSONRenderer().render(res)
            return HttpResponse(json_data , content_type='application/json')
        json_data= JSONRenderer().render(serialzers.errors)
        return HttpResponse(json_data , content_type='application/json')
@csrf_exempt
def student_delete(request):
    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        res = {'msg': 'data deleted successfully'}
        # json_data = JSONRenderer().render(res)
        # return HttpResponse(json_data,content_type='application/json')
        # (or)
        return JsonResponse(res , safe = False)