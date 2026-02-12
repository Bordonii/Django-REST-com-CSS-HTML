from rest_framework.response import Response
from rest_framework.decorators import api_view,parser_classes
from base.models import Item
from .serializers import ItemmSerializer
from rest_framework import status
from django.shortcuts import render, get_object_or_404
from rest_framework.parsers import MultiPartParser, FormParser




@api_view(['GET'])
def get_data(request):
    items = Item.objects.all()
    serializer = ItemmSerializer(items, many= True)
    return Response(serializer.data)


@api_view((['POST']))
@parser_classes([MultiPartParser, FormParser])
def addItem(request):
    serializer = ItemmSerializer(data= request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
    return Response(serializer.data)


@api_view(['PUT'])
def putItem(request, pk):
    item = get_object_or_404(Item, id=pk)
    serializer = ItemmSerializer(item, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response({
            "success": True,
            "message": "Item atualizado",
            "data": serializer.data
        }, status=200)
    
    return Response({
        "success": False,
        "errors": serializer.errors
    }, status=400)


@api_view(['DELETE'])
def delete_item_api(request, pk):
    item = get_object_or_404(Item, id=pk)
    serializer = ItemmSerializer(item)
    item.delete()
    return Response(
        {"message": "Item deletado", "deleted_item": serializer.data},
        status=status.HTTP_200_OK
    )


def home(request):
    from base.models import Item
    itens = Item.objects.all()
    print("ITENS DA VIEW:", itens.count()) 
    return render(request, 'site/home.html', {'itens': itens})