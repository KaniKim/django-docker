from billing.models import Invoice, ItemLine
from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    id = serializers.CharField()
    name = serializers.CharField()
    email = serializers.CharField()


class ItemLineSerializer(serializers.Serializer):
    quantity = serializers.IntegerField()
    description = serializers.CharField()
    price = serializers.IntegerField()
    taxed = serializers.BooleanField()


class InvoiceSerializer(serializers.Serializer):
    user = UserSerializer
    date = serializers.DateTimeField()
    due_date = serializers.DateTimeField()
    items = ItemLineSerializer(many=True)

    def create(self, validated_data):
        items = validated_data.pop("items")
        invoice = Invoice.objects.create(**validated_data)

        for item in items:
            ItemLine.objects.create(invoice=invoice, **item)

        return invoice
