from django.shortcuts import render
from rest_framework import views
from .models import Department
from django.db.models import Q
from .serializers import DepartmentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.


class DepartmentView(APIView):

    def get(self, request):
        name = request.GET.get(key='name', default="")
        departments = Department.objects.filter(Q(full_name__icontains=name) | Q(short_name__icontains=name))
        departments_serializer = DepartmentSerializer(departments, many=True)
        return Response(departments_serializer.data)

    def post(self, request):
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SpecificDepartmentView(APIView):

    def get(self, request, department_id):
        department = Department.objects.get(pk=department_id)
        department_serializer = DepartmentSerializer(department)
        return Response(department_serializer.data)

    def delete(self, request, department_id):
        Department.objects.filter(pk=department_id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, department_id):
        department_old = Department.objects.get(pk=department_id)
        serializer = DepartmentSerializer(department_old, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
