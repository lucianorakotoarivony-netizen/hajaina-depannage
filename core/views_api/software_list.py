from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Software
from ..serializers import SoftwareSerializer

@api_view(["GET"])
def get_software_list(request):
    software_list=Software.available.all()
    serializer=SoftwareSerializer(software_list, many=True)
    return Response(serializer.data)
