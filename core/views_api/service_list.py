from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Service
from ..serializers import ServiceSerializer

@api_view(["GET"])
def get_service_list(request):
    services=Service.available.all()
    serializer=ServiceSerializer(services, many=True)
    return Response(serializer.data)
