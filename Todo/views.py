from django.shortcuts import render,redirect,get_object_or_404
from .models import Task
from .forms import TaskForm

# Create your views here.

# for get all data and redirect from the templates
def task_list(request):
    task = Task.objects.all() # to get all data
    return render(request, 'todo/task_list.html', {'task' : task})

# create 

def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)  # Correct form class
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'todo/task_form.html', {'form': form})  # Use a separate template
    
# update

def task_update(request,pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task) 
    return render(request, 'todo/task_form.html', {'form': form})


# delete

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'todo/task_delete.html', {'task': task})
