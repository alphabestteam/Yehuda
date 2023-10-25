from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from .serializers import UserSerializer
from .models import User


@api_view(["POST"])  
def add_user(request):
    object_data = request.data
    data_deserialized = UserSerializer(data=object_data)
    if data_deserialized.is_valid():
        data_deserialized.save()
        return Response("The user saved!")
    return Response("Something want wrong")


@api_view(["PUT"]) 
def update_user(request):
    data = request.data 
    user_id = data["user_id"]
    user = get_object_or_404(User, user_id=user_id)
    user_serialized = UserSerializer(user, data=data)
    if user_serialized.is_valid():
        user_serialized.save()
        return Response("the user updated!")
    return Response("Something in update user want wrong!")


@api_view(["DELETE"])
def delete_user(request, id):
    user = get_object_or_404(User, user_id=id)
    user.delete()
    return Response("The user was deleted!")


@api_view(["GET"])
def all_users(request):
    user = User.objects.all()
    user_serialized = UserSerializer(user, many=True)
    return Response(user_serialized.data)
