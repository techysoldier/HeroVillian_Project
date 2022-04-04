

# Create your views here.
from super_types.models import Super_type
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from supers.models import Super
from supers.serializers import SuperSerializer
from django.shortcuts import get_object_or_404


# Create your views here.

@api_view(['GET'])

def super_type_list(request):

    appending_dict_example = {}
    appending_dict_example['name'] = 'Bob'
    print(appending_dict_example)

    super_types = Super_type.objects.all()
    
    custom_response_dictionary = {}

    for super_types in super_types:

        supers = Super.objects.filter(supers_id=supers.id)

        supers_serializer = SuperSerializer(supers, many=True)

        custom_response_dictionary[super_types.name] = {
            "address": super_types.address,
            "supers": supers_serializer.data
        }
    return Response(custom_response_dictionary)