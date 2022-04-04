from super_types.models import Super_type
from rest_framework.decorators import api_view
from rest_framework.response import Response
from supers.models import Super
from supers.serializers import SuperSerializer



@api_view(['GET'])
def super_type_list(request):

    appending_dict_example = {}
    appending_dict_example['name'] = 'villian'
    print(appending_dict_example)

    super_types = Super_type.objects.all()
    
    custom_response_dictionary = {}

    for super_types in super_types:

        supers = Super.objects.filter(super_id=super.id)

        supers_serializer = SuperSerializer(supers, many=True)

        custom_response_dictionary[super_types] = {
            "type": super_types,
            "super": supers_serializer.data
        }
    return Response(custom_response_dictionary)