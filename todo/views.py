from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate

# Create your views here.
from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm, SignUpForm


# Create your views here.
def index(request):
    return redirect('Task-list')


def TaskList(request, priority=None):
    if priority is not None:
        if priority == "low":
            Tasks = Task.objects.filter(user=request.user, priority='L')
        elif priority == "medium":
            Tasks = Task.objects.filter(user=request.user, priority='M')
        elif priority =="high":
            Tasks = Task.objects.filter(user=request.user, priority='H')
    else:
        Tasks = Task.objects.filter(user=request.user)
    return render(request, "home.html", {'Tasks': Tasks})


def TaskCreate(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            print("aaaaa")
            try:
                form.instance.user = request.user
                form.save()
                print("bbbbbbbb")
                model = form.instance
                return redirect('Task-list')
            except Exception as e:
                print(e)
                print(form.errors)
                pass
    else:
        form = TaskForm()
    return render(request, 'create.html', {'form': form})


def TaskUpdate(request, id):
    task = Task.objects.get(id=id)
    form = TaskForm(initial={'title': task.title,
                             'description': task.description,
                             'completed': task.completed,
                             'due_date': task.due_date,
                             'priority': task.priority})
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('/Task-list')
            except Exception as e:
                pass
    return render(request, 'update.html', {'form': form})


def TaskDelete(request, id):
    task = Task.objects.get(id=id)
    try:
        task.delete()
    except Exception as e:
        pass
    return redirect('Task-list')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('Task-list')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
