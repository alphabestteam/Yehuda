from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from targets.models import Target
from targets.serializers import TargetSerializer

@csrf_exempt
def add_target(request):
        if request.method == 'POST':
            object_data = JSONParser().parse(request)
            data_deserialized = TargetSerializer(data= object_data)
            if data_deserialized.is_valid():
                data_deserialized.create(object_data).save()
                return HttpResponse("save successfully!" )
            else:
                return HttpResponse("not well formed " )
        else:
            return HttpResponse("not post")
   

        
@csrf_exempt
def update_target(request):
    # Implement here an update function
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        target = Target.objects.get(pk=data['target_id'])  
        serializer = TargetSerializer(target, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Target updated successfully!", safe= False)
        else:
            return HttpResponse("Invalid data", status=400)
    else:
        return JsonResponse("This endpoint only accepts POST requests", safe= False)
   

def all_targets(request):
    # Implement here a get all targets function
    target = Target.objects.all()
    target_serialized = TargetSerializer(target,many =True)
    return JsonResponse(target_serialized.data , safe=False)