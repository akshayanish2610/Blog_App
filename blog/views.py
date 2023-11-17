from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from blog.models import BlogModel,BlogRegistration
from blog.serialiser import BlogSerializer,RegSerializer
from django.http import HttpResponse
from django.db.models import Q

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
        
@csrf_exempt
def ViewMyPost(request):
    if request.method=="POST":
        recieved_data=json.loads(request.body)
        getUser_id=recieved_data["user_id"]
        data=list(BlogModel.objects.filter(Q(use_id__icontains=getUser_id)).values())
        return HttpResponse(json.dumps(data))
    

@csrf_exempt
def Registration(request):
    if request.method == "POST":
        recievedData=json.loads(request.body)
        print(recievedData)
        serializer_check=RegSerializer(data=recievedData)
        if serializer_check.is_valid():
            serializer_check.save()
            return HttpResponse(json.dumps({"status":"Success"}))
        else:
            return HttpResponse(json.dumps({"status":"Failed"}))