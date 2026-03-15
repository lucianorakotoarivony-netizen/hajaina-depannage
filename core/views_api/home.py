from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Home
from ..serializers import HomeSerializer

@api_view(["GET"])
def get_home_data(request):
    config_home=Home.load()
    serializer=HomeSerializer(config_home)
    return Response(serializer.data)
