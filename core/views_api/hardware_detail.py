
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Hardware
from ..serializers import HardwareSerializer
from django.shortcuts import get_object_or_404

@api_view(["GET"])
def get_hardware_detail(request, pk):
    hardware=get_object_or_404(Hardware,pk=pk)
    serializer=HardwareSerializer(hardware)
    return Response(serializer.data)
    