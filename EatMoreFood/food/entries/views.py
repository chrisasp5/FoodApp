from django.shortcuts import render, redirect
from .models import Entry, NewFood
from .forms import EntryForm, NewFoodForm

# def index(request):
#     entries = Entry.objects.order_by('-date_posted')
#
#     context = {'entries' : entries}
#
#     return render(request, 'entries/index.html', context)
#
# def add(request):
#     if request.method == 'POST':
#         form = EntryForm(request.POST)
#
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = EntryForm()
#
#     context = {'form' : form}
#
#     return render(request, 'entries/add.html', context)
def add(request):

    return render(request, 'entries/add.html')

def index(request):

    return render(request, 'entries/index.html')

def login(request):

    return render(request, 'entries/login.html')

def signup(request):

    return render(request, 'entries/signup.html')

def form(request):

    return render(request, 'entries/form.html')

def home(request):

    return render(request, 'entries/home.html')

def new(request):

    return render(request, 'entries/new.html')

def added(request):

    return render(request, 'entries/added.html')

def past(request):

    return render(request, 'entries/past.html')
# def new(request):
#         if request.method == 'POST':
#             form = NewFoodForm(request.POST)
#
#             if form.is_valid():
#                 New_Food = NewFood(name=request.POST['name'], rating=request.POST['rating'],comments=request.POST['comments'])
#                 New_Food.save()
#                 return redirect('added')
#         else:
#             form = NewFoodForm()
#
#         context = {'form' : form}
#
#         return render(request, 'food/new.html', context)
#
# def past(request):
#     newfoods = NewFood.objects.order_by('-date_added')
#
#     context = {'newfoods' : newfoods}
#
#     return render(request, 'food/past.html', context)
#
# def home(request):
#
#     return render(request, 'food/home.html')
#
# def added(request):
#
#     return render(request, 'food/added.html')
