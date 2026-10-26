from django.shortcuts import render,redirect
from app.models import task
# Create your views here.
def home(request):
    tasks=task.objects.filter(is_completed=False)
    completed_task=task.objects.filter(is_completed=True)
    return render(request,'app/home.html',{"tasks":tasks,'completed_task':completed_task})
def addtask(request):
    if request.method=="POST":
        task2=request.POST.get("task")
        task1=task(task=task2)
        task1.save()
        return redirect('/')
    return render(request,'app/home.html')
def complete(request,id):
    Task=task.objects.get(id=id)
    Task.is_completed=True
    Task.save()
    return redirect('/')
def incomplete(request,id):
    Task=task.objects.get(id=id)
    Task.is_completed=False
    Task.save()
    return redirect('/')
def update(request,id):
    d=task.objects.get(id=id)
    if request.method=="POST":
        task1=request.POST.get("task")
        x=task.objects.get(id=id)
        x.task=task1
        x.save()
        return redirect('/')
    return render(request,'app/edit.html',{"d":d})
def delete(request,id):
    d=task.objects.get(id=id)
    d.delete()
    return redirect('/')