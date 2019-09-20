from django.shortcuts import render, redirect
from .models import Entry
from .forms import EntryForm

def index(request):
    entries = Entry.objects.order_by('-date_posted')

    context = {'entries' : entries}

    return render(request, 'entries/index.html', context)

def add(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EntryForm()

    context = {'form' : form}

    return render(request, 'entries/add.html', context)

def past(request):
    newfoods = NewFood.objects.order_by('-date_added')

    context = {'newfoods' : newfoods}

    return render(request, 'food/past.html', context)

def new(request):
    if request.method == 'POST':
        form = NewFoodForm(request.POST)

        if form.is_valid():
            New_Food = NewFood(name=request.POST['name'], rating=request.POST['rating'],comments=request.POST['comments'])
            New_Food.save()
            return redirect('past')

    else:
        form = NewFoodForm()

    context = {'form' : form}
    return render(request, 'food/new.html', context)
