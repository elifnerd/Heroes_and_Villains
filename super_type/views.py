from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SuperTypeSerializer
from .models import SuperType

@api_view(['GET'])
def super_type_list(request):
    super_types = SuperType.objects.all()
    serializer = SuperTypeSerializer(super_types, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def super_type_detail(request, pk):
    
    print(pk)
    return Response((pk))