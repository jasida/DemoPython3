from django.http import HttpResponse
from django.shortcuts import render

from . models import Teams
from . models import Members
def demo(request):
    objec=Members.objects.all
    obj=Teams.objects.all
    context={
        'result': obj,
        'res': objec

    }
    return render(request, "index.html",context)
