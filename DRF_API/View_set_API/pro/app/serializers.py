from rest_framework import serializers
from app.models import Student , officers


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class OfficersSerializer(serializers.ModelSerializer):
    class Meta:
        model = officers
        fields = '__all__'
        