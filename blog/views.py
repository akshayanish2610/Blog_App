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
    


    

