from rest_framework import serializers
from .models import Department, Person


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class PersonSerialized(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

