from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import Team
# Create your views here.
def index(request):
    obj=Place.objects.all()
    people=Team.objects.all()
    return render(request,"index.html",{'result':obj,'team':people})

def page(request):
   #country='kerala'
  return render(request,"index1.html")
#def addition(request):
  #  x=int(request.GET['num1'])
  #  y=int(request.GET['num2'])
  #  res=x+y
   # return render(request,"result.html",{'result':res})

#def about(request):
#    return render(request,"about.html")

#def response(request):
 #   return HttpResponse("i am here respond")


