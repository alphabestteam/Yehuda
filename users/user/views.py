from django.shortcuts import render
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
import json


@api_view(["GET"])
def all_user(request):
    people = User.objects.all()
    people_serialized = UserSerializer(people, many=True)
    return Response(people_serialized.data)


@api_view(["POST"])
def add_user(request):
    if request.method == "POST":
        data_deserialized = UserSerializer(data=request.data,partial = True)
        if data_deserialized.is_valid():
            data_deserialized.save()
            return Response("User created successfully!")
        else:
            return Response(data_deserialized.errors)
    else:
        return Response("Method not allowed")


@api_view(["DELETE"])
def del_user(request, id):
    user = get_object_or_404(User, id=id)
    user.delete()
    return Response("the object del")


@api_view(["GET"])
def find_user(request, id):
    if request.method == "GET":
        user = get_object_or_404(User, id=id)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    else:
        return Response("You need to use the GET method")


@api_view(["POST"])
def chang_password(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_id = data.get("id")
        new_password = data.get("password")
        try:
            user = User.objects.get(id=user_id)
            user.set_password(new_password)
            user.save()
            return Response("Password changed successfully!")
        except User.DoesNotExist:
            return Response("User not found")
    else:
        return Response("Method not allowed")
