from django.shortcuts import render, redirect

names = [
    {
        'name': 'K Satish Kumar',
        'age' : 23
    },
    {
        'name': 'K Somnadh',
        'age' : 24
    },
    {
        'name': 'K Lakshmi Narayana',
        'age' : 25
    },
    {
        'name': 'M Sai Ramya',
        'age' : 22
    }
]

def index(request):
    return redirect('home')

def home(request):
    context = {
        'names': names
    }
    return render(request, 'index.html', context)
