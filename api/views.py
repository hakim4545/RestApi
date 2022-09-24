from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Item 
from .serializers import ItemSerializer

@api_view(['GET'])
def getData(request):
    # Pipes ={'Name':'Jala Pipes','size':'35MM','Qty':'50'}
    items=Item.objects.all()
    serializer=ItemSerializer(items,many=true)
    return Response(serializer.data)


