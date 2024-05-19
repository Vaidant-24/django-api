from django.shortcuts import render,HttpResponse
from rest_framework import viewsets
from API.models import Company,Employee,Student,School
from API.serializers import CompanySerializer,EmployeeSerializer,StudentSerializer,SchoolSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


# Create your views here.
def home(request):
    return HttpResponse("<h1>Welcome to API</h1>")

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    #company/{companyId}/employee
    @action(detail = True, methods = ['GET'])
    def employee(self, request, pk=None):
        try:
            cmpy = Company.objects.get(pk=pk)
            emps = Employee.objects.filter(company=cmpy)
            emps_serializer = EmployeeSerializer(emps , many = True , context = {'request':request})
            return Response(emps_serializer.data)
        except Exception as e:
            print(e)
            return Response({'message':'Company might not exist!'})
        
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    @action(detail=True,methods=['GET'])
    def student(self,request,pk=None):
        sch = School.objects.get(pk=pk)
        stu = Student.objects.filter(school=sch)
        stu_serializer = StudentSerializer(stu , many=True, context = {'request': request})
        return Response(stu_serializer.data)
    
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

