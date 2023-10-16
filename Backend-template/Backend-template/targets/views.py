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
                data_deserialized.save()
                return HttpResponse("save successfully!" )
            else:
                return HttpResponse("not well formed" )
        else:
            return HttpResponse("not post")
   

        
# @csrf_exempt
# def update_target(request):
#     # Implement here an update function

def all_targets(request):
    # Implement here a get all targets function
    target = Target.objects.all()
    target_serialized = TargetSerializer(target,many =True)
    return JsonResponse(target_serialized.data , safe=False)