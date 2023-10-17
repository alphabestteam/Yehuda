from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse ,JsonResponse
from rest_framework.parsers import JSONParser
from .models import Person
from .serializers import PeopleSerializer


@csrf_exempt
def all_people(request):
    if request.method == 'GET':
        people = Person.objects.all()
        people_serialized = PeopleSerializer(people,many =True)
        return JsonResponse(people_serialized.data , safe=False , status=200)
    else:
        return HttpResponse("you need the change method " ,status =101)

@csrf_exempt
def add_people(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        data_deserialized = PeopleSerializer(data=data)
        if data_deserialized.is_valid():
            data_deserialized.save()
            return HttpResponse("save successfully!",status=201)
        else:
            return HttpResponse("not well formed", status=406)
    else:
            return HttpResponse("not post" , status=101)

@csrf_exempt
def del_people(request,id):
    if request.method == 'DELETE':
        try:
            instance = Person.objects.get(id=id)
            instance.delete()
            return HttpResponse("the object del", status=202)
        except:
            return HttpResponse("the object is not exist", status=404)
    else:
        return HttpResponse("you need the change method " ,status =101)

       

@csrf_exempt
def update_people(request):
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        try:
            target = Person.objects.get(pk=data['id'])  
        except target.DoesNotExist:
            return JsonResponse ("the target do not exist !" , status = 404)
        serializer = PeopleSerializer(target, data=data)

        if serializer.is_valid():
            serializer.update()
            return JsonResponse("person updated successfully!", safe= False , status=200 )
        else:
            return HttpResponse("Invalid data", status=400)
    else:
        return JsonResponse("This endpoint only accepts POST requests", safe= False,status= 101)

# Create your views here.
