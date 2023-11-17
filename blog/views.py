from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from blog.models import BlogModel
from blog.serialiser import BlogSerializer
from django.http import HttpResponse

# Create your views here.

@csrf_exempt
def Viewall(request):
    if request.method =="POST":
        BlogList=BlogModel.objects.all()
        serialise_data=BlogSerializer(BlogList,many=True)
        return HttpResponse(json.dumps(serialise_data.data))
    

@csrf_exempt
def AddPost(request):
    if request.method == "POST":
        recievedData=json.loads(request.body)
        print(recievedData)
        serializer_check=BlogSerializer(data=recievedData)
        if serializer_check.is_valid():
            serializer_check.save()
            return HttpResponse(json.dumps({"status":"Success"}))
        else:
            return HttpResponse(json.dumps({"status":"Failed"}))

    

