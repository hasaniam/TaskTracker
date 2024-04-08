from django.shortcuts import render
from django .http import HttpResponse

my_task =list()
def home(request):
    #return HttpResponse('<h1>This is home page</h1>')

    if request.method =="POST":
        task = request.POST.get("task")
        my_task.append(task)

    context ={
        "tasks": my_task,
    }
    return render(request, 'home.html', context)

def login(request):
    #return HttpResponse('<h1>This is login page</h1>')
    return render(request, 'login.html', {})
def register(request):
    #return HttpResponse('<h1>This is register page</h1>')
    return render(request, 'register.html', {})



