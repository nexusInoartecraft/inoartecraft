#from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Student
from django.template import loader
from django.shortcuts import render

def index(request):
    return HttpResponse("Bem vindo ao Inoartecraft")

def detail(request, id):
    Student_list = Student.objects.all()
    template = loader.get_template ("inoartecraft/details.html")
    context = {
        "Student_list" : Student_list
    }
    #return render(request, "inoartecraft/details.html", context)
    return HttpResponse(template.render(context,request))

# Leave the rest of the views (detail, results, vote) unchanged

