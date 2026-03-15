from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Hardware
from ..serializers import HardwareSerializer

@api_view(["GET"])
def get_hardware_list(request):
    hardware_list=Hardware.available.all()
    serializer=HardwareSerializer(hardware_list, many=True)
    return Response(serializer.data)
