from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.


def members(request) -> HttpResponse:
    template = loader.get_template("myfrist.html")
    
    return HttpResponse(template.render())