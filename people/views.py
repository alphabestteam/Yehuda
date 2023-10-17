from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse ,JsonResponse
from rest_framework.parsers import JSONParser
from .models import Person
from .serializers import PeopleSerializer

@csrf_exempt
def add_people(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        data_deserialized = PeopleSerializer(data=data)
        if data_deserialized.is_valid():
            data_deserialized.save()
            return HttpResponse("save successfully!")
        else:
            return HttpResponse("not well formed")
    else:
            return HttpResponse("not post")

@csrf_exempt
def del_people(request,id):
    try:
        instance = Person.objects.get(id=id)
        instance.delete()
        return HttpResponse("the object del")
    except:
        return HttpResponse("the object is not exist")
       

@csrf_exempt
def update_people(request):
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        target = Person.objects.get(pk=data['id'])  
        serializer = PeopleSerializer(target, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Target updated successfully!", safe= False)
        else:
            return HttpResponse("Invalid data", status=400)
    else:
        return JsonResponse("This endpoint only accepts POST requests", safe= False)

# Create your views here.
