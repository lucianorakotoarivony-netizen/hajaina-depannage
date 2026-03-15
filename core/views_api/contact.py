from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Contact
from ..serializers import ContactSerializer

@api_view(["GET"])
def get_contact_data(request):
    contact_data=Contact.load()
    serializer=ContactSerializer(contact_data)
    return Response(serializer.data)
    

    
