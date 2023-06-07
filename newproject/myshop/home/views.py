from django.shortcuts import render , redirect
from .forms import SignupForm
from item.models import *
from django.contrib.auth import logout
# Create your views here.
def homepage(request):
    items = Item.objects.all()
    return render(request , 'homepage.html', {'items':items})

def contact(request):
    return render(request , 'contact.html', {})

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'signup.html', {
        'form': form
    })
