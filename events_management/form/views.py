from .models import Event ,Event_file,Event_chat
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import EventSerializer, EventFileSerializer,EventChatSerializer
from django.shortcuts import get_object_or_404

######################################### regular event ###############################################
@api_view(['GET'])
def event_list(request):
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def event_add(request):
    serializer = EventSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def event_del(request,pk):
    event = get_object_or_404(Event, pk=pk)
    event.delete()
    return Response('the user delete',status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
def event_up(request,pk):
    event = get_object_or_404(Event, pk=pk)
    serializer = EventSerializer(event, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def event_find(request,pk):
    event = get_object_or_404(Event, pk=pk)
    serializer = EventSerializer(event)
    return Response(serializer.data)


######################################### file event ###############################################


@api_view(['GET'])
def event_file_list(request):
    events = Event_file.objects.all()
    serializer = EventFileSerializer(events, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def event_file_add(request):
    serializer = EventFileSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def event_file_del(request,pk):
    event = get_object_or_404(Event_file, pk=pk)
    event.delete()
    return Response('the user delete',status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
def event_file_up(request,pk):
    event = get_object_or_404(Event_file, pk=pk)
    serializer = EventFileSerializer(event, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def event_file_find(request,pk):
    event = get_object_or_404(Event_file, pk=pk)
    serializer = EventFileSerializer(event)
    return Response(serializer.data)

######################################### chat event ###############################################

@api_view(['GET'])
def event_chat_list(request):
    events = Event_chat.objects.all()
    serializer = EventChatSerializer(events, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def event_chat_add(request):
    serializer = EventChatSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def event_chat_del(request,pk):
    event = get_object_or_404(Event_chat, pk=pk)
    event.delete()
    return Response('the user delete',status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
def event_chat_up(request,pk):
    event = get_object_or_404(Event_chat, pk=pk)
    serializer = EventChatSerializer(event, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def event_chat_find(request,pk):
    event = get_object_or_404(Event_chat, pk=pk)
    serializer = EventChatSerializer(event)
    return Response(serializer.data)

