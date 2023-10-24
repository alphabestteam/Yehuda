from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from rest_framework import serializers,status
from .serializer import userSerializer


@api_view(['POST'])
def add_user(request):
    user = userSerializer(data=request.data)
    if User.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
    if user.is_valid():
        user.save()
        return Response(user.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
def view_user(request):
    
    if request.query_params:
        items = User.objects.filter(**request.query_params.dict())
    else:
        items = User.objects.all()
 
    if items:
        serializer = userSerializer(items, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def update_user(request, pk):
    item = User.objects.get(pk=pk)
    data = userSerializer(instance=item, data=request.data)
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_user(request, pk):
    item = get_object_or_404(User, pk=pk)
    item.delete()
    return Response(status=status.HTTP_202_ACCEPTED)