from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddNewUser
from .models import Record
# Create your views here.

def home(request):
    if request.user.is_authenticated :
        records = Record.objects.all()
        return render(request, 'home.html', {'records':records})
    else :
        return redirect("login")
    return render(request, 'home.html')

def login_user(request):
    if request.user.is_authenticated:
        messages.success(request, "You are already logged in")
        return redirect("home")
    else : 
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            # Check if the information is correct
            user = authenticate(request, username= username, password= password)
            if user is not None :
                login(request, user)
                messages.success(request, "You have been logged in successfuly")
                return redirect("home")
            else :
                messages.success(request, "The username or the password is incorrect")
                return redirect("login")
    # rendering the login page that appear in the web page
    return render(request, 'login.html')
        
def logout_user(request):
    logout(request, )
    messages.success(request, "You have been logged out ..")
    return redirect("home")

def register_user(request):
    if request.user.is_authenticated:
        messages.success(request, "You are already logged in")
        return redirect("home")
    else :
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                # Authenticate and login
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']
                user = authenticate(username=username, password=password)
                login(request, user)
                messages.success(request, "You have been Successfuly Register")
                return redirect('home')
        else: 
            form = SignUpForm()
        return render(request, 'register.html', {"form":form})

def customer_record(request, pk):
    if request.user.is_authenticated :
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record':customer_record})
    else :
        messages.success(request, "You Must Be Logged In")
        return redirect("home")

def DeleteRecord(request, pk):
    # Check if the user is already logged in 
    if request.user.is_authenticated :
        # Delete the user that admin chosse to delete it
        user_delted = Record.objects.get(id=pk)
        user_delted.delete()
        messages.success(request, "User Has Been Deleted Succesfully...😁")
        return redirect("home")
    else :
        messages.success(request, "You Must Be Logged In..!!")
        return redirect("login")
    
def AddUser(request):
    form = AddNewUser(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "The User Has Been Add Succesfully")
                return redirect("home")
        return render(request, "AddUser.html", {"form":form})
    else :
        messages.success(request, "You Must Be Logged In ...!!")
        return redirect("login")