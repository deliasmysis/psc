from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm



def register(request): 
    form = UserCreationForm() 
    if request.method == 'POST':  
        form = UserCreationForm(request.POST)  
        if form.is_valid():
            form.save()  
            return redirect('login')
        else:
            return render(request, 'er.html', {'msg':['Error']})
    
    return render(request, 'register.html', {'form':form })  

def Login(request):
    if request.method == "POST":
        username = request.POST['user']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'er.html', {'msg':['The sign-in ID or password is not correct.']})
    return render(request, 'login.html')


@login_required(login_url='/login')
def home(request):
    return render(request, 'home.html')

@login_required(login_url='/login')
def power(request):
    return render(request, 'power.html')


@login_required(login_url='/login')
def Logout(request):
    logout(request)
    return redirect('login')