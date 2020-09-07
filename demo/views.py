from django.shortcuts import render
from .models import Demo
from json import dumps 
import json
from django.core import serializers
# Create your views here.
def Homeview(request):

    data = Demo.objects.all()
    #js_data = dumps(data)

    js_data = serializers.serialize('json', data)

    return render(request, 'visaogeral.html', {"data": js_data})

