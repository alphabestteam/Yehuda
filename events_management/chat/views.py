from .models import message ,Chat
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import MessageSerializer,ChatSerializer
from django.shortcuts import get_object_or_404

###################################################### chat ##################################
 
@api_view(['GET'])
def event_chat_list(request):
    events = Chat.objects.all()
    serializer = ChatSerializer(events, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def event_chat_add(request):
    serializer = ChatSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def event_chat_del(request,pk):
    event = get_object_or_404(Chat, pk=pk)
    event.delete()
    return Response('the user delete',status=status.HTTP_204_NO_CONTENT)

############################################# message ###############################

@api_view(['GET'])
def event_message_list(request):
    events = message.objects.all()
    serializer = MessageSerializer(events, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def event_message_add(request):
    serializer = MessageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def event_message_del(request,pk):
    event = get_object_or_404(message, pk=pk)
    event.delete()
    return Response('the user delete',status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
def event_message_up(request,pk):
    event = get_object_or_404(message, pk=pk)
    serializer = MessageSerializer(event, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def event_message_find(request,pk):
    event = get_object_or_404(message, pk=pk)
    serializer = MessageSerializer(event)
    return Response(serializer.data)
