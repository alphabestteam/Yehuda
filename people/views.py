from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse ,JsonResponse
from rest_framework.parsers import JSONParser
from .models import Person,Parent
from .serializers import PeopleSerializer,parentSerializer
from django.db.models import Q


@csrf_exempt
def all_people(request):
    people = Person.objects.all()
    people_serialized = PeopleSerializer(people,many =True)
    return JsonResponse(people_serialized.data , safe=False)

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
            return JsonResponse("person updated successfully!", safe= False)
        else:
            return HttpResponse("Invalid data", status=400)
    else:
        return JsonResponse("This endpoint only accepts POST requests", safe= False)

# parent function.

@csrf_exempt
def all_parent(request):
    if request.method == 'GET':
        parents = Parent.objects.all()
        parent_serialized = parentSerializer(parents,many =True)
        return JsonResponse(parent_serialized.data , safe=False , status=200)
    else:
        return HttpResponse("you need the change method " ,status =101)

@csrf_exempt
def add_parent(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        data_deserialized = parentSerializer(data=data)
        print(data)
        if data_deserialized.is_valid():
            data_deserialized.save()
            return HttpResponse("save successfully!",status=201)
        else:
            return HttpResponse("not well formed", status=406)
    else:
            return HttpResponse("not post" , status=101)

@csrf_exempt
def del_parent(request,id):
    if request.method == 'DELETE':
        try:
            instance = Parent.objects.get(id=id)
            instance.delete()
            return HttpResponse("the object del", status=202)
        except:
            return HttpResponse("the object is not exist", status=404)
    else:
        return HttpResponse("you need the change method " ,status =101)

       

@csrf_exempt
def update_parent(request):
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        try:
            parent = Parent.objects.get(pk=data['id'])  
        except Parent.DoesNotExist:
            return JsonResponse ("the parent do not exist !" , status = 404)
        serializer = parentSerializer(parent, data=data)

        if serializer.is_valid(): 
            serializer.save()
            return JsonResponse("parent updated successfully!", safe= False , status=200 )
        else:
            return HttpResponse("Invalid data", status=400)
    else:
        return JsonResponse("This endpoint only accepts POST requests", safe= False,status= 101)

@csrf_exempt
def Connect_Child_Parent(request):
    if request.method == 'PUT':  
        data = JSONParser().parse(request)
        try:
            parent = Parent.objects.get(id=data['id_parent']) 
        except:
            return JsonResponse("the parent do not exist !" , status = 404, safe= False) 
        try:
            child= Person.objects.get(id=data['id_child'])        
        except:
            return JsonResponse("the child do not exist !" , status = 404, safe= False)
        
        parent.child.add(child)
        return HttpResponse("the child is yours ( :")
    else:
        return JsonResponse("This endpoint only accepts POST requests", safe= False,status= 101)
    
@csrf_exempt
def parent_and_child(request):
    if request.method == 'GET':
        data = JSONParser().parse(request)
        try:
            parent = Parent.objects.get(pk=data["id"])
        except Parent.DoesNotExist:
            return JsonResponse( "The parent does not exist", safe=False, status=404)
        
        parent_serialized = parentSerializer(parent).data  
        
        children = parent.child.all() 
        child_serialized = []
        
        for child in children:
            child_data = PeopleSerializer(child).data
            child_serialized.append(child_data)
        
        return JsonResponse([parent_serialized,child_serialized], safe=False, status=200)
    else:
        return HttpResponse("You need to use the GET method", status=405)
    
@csrf_exempt
def rich_kid(request):
    if request.method == 'GET':
        try:
            parent = Parent.objects.filter(salary__gt=40000)  
        except Parent.DoesNotExist:
            return JsonResponse("No parents with a salary greater than 40 found", safe=False, status=404)
            
        children = Person.objects.filter(child__in=parent, date_of_birth__gt='2005-01-01')
        child_serialized = []
        
        for child in children:   
            child_data = PeopleSerializer(child).data
            child_serialized.append(child_data)
        
        return JsonResponse(child_serialized, safe=False, status=200)
    else:
        return HttpResponse("You need to use the GET method", status=405)

@csrf_exempt
def find_parent(request , id):
    if request.method == 'GET':
        try:
            child = Person.objects.get(id=id)  
        except Person.DoesNotExist:
            return JsonResponse("No parents found for this child", safe=False, status=404)
        
        parent = parentSerializer(child.parents.all(), many=True).data  
        
        return JsonResponse(parent, safe=False, status=200)
    else:
        return HttpResponse("You need to use the GET method", status=405)
    
@csrf_exempt
def find_son(request , id):
    if request.method == 'GET':
        try:
            parent = Parent.objects.get(id=id)  
        except Parent.DoesNotExist:
            return JsonResponse("No siblings found for this person", safe=False, status=404)
        
        children = parent.child.all() 
        child_data = PeopleSerializer(children , many=True ).data
 
        return JsonResponse(child_data, safe=False, status=200)
    else:
        return HttpResponse("You need to use the GET method", status=405)

def find_grandfather(request , id):
    if request.method == 'GET':
        try:
            child = Person.objects.get(id=id)  
        except Person.DoesNotExist:
            return JsonResponse("No parents found for this child", safe=False, status=404)
        
        parent = child.parents.all()
        for grand in parent :   
            grandfather =parentSerializer(grand.parents.all(), many=True).data  
        
        return JsonResponse(grandfather, safe= False,  status=200)
    else:
        return HttpResponse("You need to use the GET method", status=405)

def find_Siblings(request , id):
    if request.method == 'GET':
        try:
            person = Person.objects.get(id=id)
        except Person.DoesNotExist:
            return JsonResponse( "The person do not exist", safe=False, status=404)

        siblings = Person.objects.filter(parents__in=person.parents.all())
        sibling_serialized = PeopleSerializer(siblings, many=True).data

        return JsonResponse(sibling_serialized, safe=False, status=200)
    else:
        return HttpResponse("You need to use the GET method", status=405)
    
        

    
# Create your views here.