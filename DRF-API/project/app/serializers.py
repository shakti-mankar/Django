from rest_framework import serializers

class StundentSerializers(serializers.Serializers):
    Name = serializers.Charfield()
    Email = serializers.Emailfield()
    Contact = serializers.Intergerfield()
    Age = serializers.Intergerfield()
    