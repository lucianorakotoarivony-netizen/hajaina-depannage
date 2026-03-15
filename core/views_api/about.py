from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import About
from ..serializers import AboutSerializer

@api_view(["GET"])
def get_about_data(request):
    about_data=About.load()
    serializer=AboutSerializer(about_data)
    return Response(serializer.data)
