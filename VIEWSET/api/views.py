from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet 
from api.models import Student
from api.serializers import StudentSerializer


# Create your views here.

class StudentViewSet(ViewSet):
    def list(self, request):
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many = True)
        return Response(serializer.data)

    def retrieve(self, request ,pk = None):
        stu = Student.objects.get(pk=pk)
        serializer = StudentSerializer(stu)
        return Response(serializer.data)
    
    def create(self, request ):
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Student Created Successfully!"})
        return Response(serializer.errors)

    def update(self, request, pk):
        stu = Student.objects.get(pk=pk)
        serializer = StudentSerializer(stu,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Complete Update Successful!"})
        return Response(serializer.errors)    
    
    def partial_update(self,request ,pk):
        stu = Student.objects.get(pk=pk)
        serializer = StudentSerializer(stu,request.data,partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Partial Update Successful!"})
        return Response(serializer.errors)    
    
    def destroy(self,request,pk):
        stu = Student.objects.get(pk = pk)
        stu.delete()
        return Response({"msg": "Student Deleted Successfully!"})