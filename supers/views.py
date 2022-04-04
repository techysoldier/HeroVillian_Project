from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Super
from .serializers import SuperSerializer

@api_view(['GET'])
def super_list(request): 
        suppers = Super.objects.all()
        serializer = SuperSerializer

        return Response ('ok')