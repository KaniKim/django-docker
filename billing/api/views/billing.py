from billing.api.serializers.billing import InvoiceSerializer, UserSerializer
from user.models import User
from rest_framework.generics import CreateAPIView, ListAPIView


class ClientList(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class InvoiceCreate(CreateAPIView):
    serializer_class = InvoiceSerializer
