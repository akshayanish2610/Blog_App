from django.shortcuts import render
import json

# Create your views here.

def Viewall(request):
    if request.method =="POST":
        return (json.dumps({json.dumps({"Status":"hello"})}))
    

