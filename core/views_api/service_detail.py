
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Service
from ..serializers import ServiceSerializer
from django.shortcuts import get_object_or_404

@api_view(["GET"])
def get_service_detail(request, pk):
    service=get_object_or_404(Service,pk=pk)
    serializer=ServiceSerializer(service)
    return Response(serializer.data)
    