from django.shortcuts import render
from django.http import HttpResponse, response
from django.template import loader
from .models import Mydata

# Create your views here.


def index(request):
    mymembers = Mydata.objects.all().values()
    template = loader.get_template("index.html")
    context = {
        "mymembers": mymembers,
    }
    return HttpResponse(template.render(context, request))


def members(request):
    return render(request, "members.html")


def details(request, id):
    mymember = Mydata.objects.get(id=id)
    template = loader.get_template("details.html")
    context = {
        "mymember": mymember,
    }
    return HttpResponse(template.render(context, request))
