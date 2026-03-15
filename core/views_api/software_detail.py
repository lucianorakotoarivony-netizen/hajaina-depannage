
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Software
from ..serializers import SoftwareSerializer
from django.shortcuts import get_object_or_404

@api_view(["GET"])
def get_software_detail(request, pk):
    software=get_object_or_404(Software,pk=pk)
    serializer=SoftwareSerializer(software)
    return Response(serializer.data)