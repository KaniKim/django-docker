from list.api.serializers.list import ListSerializers
from rest_framework.generics import ListAPIView
from list.models import ListModel

class ListView(ListAPIView):
    serializer_class = ListSerializers
    queryset = ListModel.objects.all()
    
    