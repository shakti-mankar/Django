
from rest_framework import serializers
from .models import Empserialiazers


class StundentSerializers(serializers.Serializer):
    name = serializers.Charfield(max_length=30)
    email = serializers.Emailfield()
    contact = serializers.Intergerfield()
    age = serializers.Intergerfield()

    def create(self, validated_data):
        return Empserialiazers.objects.create(**validated_data)
    

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.contact = validated_data.get('contact', instance.contact)
        instance.name = validated_data.get('name', instance.name)
        instance.age = validated_data.get('age', instance.age)
        return instance
    