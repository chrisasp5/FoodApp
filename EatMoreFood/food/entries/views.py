from django.shortcuts import render, redirect
from .models import NewFood
from .forms import NewFoodForm


def index(request):
    newfoods = NewFood.objects.order_by('-date_posted')

    context = {'newfoods': newfoods}

    return render(request, 'entries/home.html', context)


def add(request):
    if request.method == 'POST':
        form = NewFoodForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('added')
    else:
        form = NewFoodForm()

    context = {'form': form}

    return render(request, 'entries/add.html', context)


def home(request):

    return render(request, 'entries/home.html')


def past(request):
    newfoods = NewFood.objects.order_by('-date_added')

    context = {'newfoods': newfoods}

    return render(request, 'entries/past.html', context)


def added(request):
    last_entry = NewFood.objects.latest('date_added')

    return render(request, 'entries/added.html', {'last_entry':last_entry})
