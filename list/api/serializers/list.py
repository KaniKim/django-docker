from rest_framework import serializers

class ListSerializers(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField()
    price = serializers.IntegerField()
    category = serializers.CharField()
    delivery_price = serializers.IntegerField()
    