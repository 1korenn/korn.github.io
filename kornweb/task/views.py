from django.shortcuts import render 
from django.http import HttpResponse ,HttpResponseRedirect
from django  import forms  
from django.urls import reverse
 
# Create your views here.



class taskform(forms.Form):
    task = forms.CharField(label="Add newtask")
    priority = forms.IntegerField(label = "priority",min_value=1 ,max_value=10)
    
def index(request):
    if "task" not in request.session:
        request.session["tasks"]=[]
    return render(request,"task/index.html",{
        "tasks": request.session["tasks"]
    })

def add(request):
    if request.method == "POST":
        form = taskform(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("task:index"))
        else:
            return render(request, "task/add.html",{
                "form": form
            })


    return render(request,"task/add.html",{
        "form": taskform()
    })