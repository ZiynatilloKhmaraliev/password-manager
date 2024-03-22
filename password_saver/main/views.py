from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.http import HttpResponse
from .forms import SignUpForm,PasswordForm
from .models import Passwords
# Create your views here.
def index(request):
    passwords=Passwords.objects.filter(user=request.user)
    return render(request,"main/index.html",{"passwords":passwords})

def signUp(request):
   
    if request.method == "POST":
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else: 
        form=SignUpForm()
    return render(request,"registration/signup.html",{"form":form})
def logoutp(request):
    
    logout(request)
    return HttpResponse("You have been logged out")

def addPassword(request):
   
    if request.method =="POST":
        form=PasswordForm(request.POST)
        if form.is_valid():
            account=form.save(commit=False)
            account.user=request.user
            account.save()
            return redirect("index")
    else:
        form=PasswordForm()
    return render(request,"main/addPassword.html",{"form":form})

def edit(request,pk):
    password=Passwords.objects.get(pk=pk)
    form=PasswordForm(instance=password)
    if request.method =="POST":
        form=PasswordForm(request.POST,instance=password)
        if form.is_valid():
            form.save()
            return redirect("index")
    return render(request,"main/edit.html",{"form":form})

def delete(request,pk):
    password=Passwords.objects.get(pk=pk)
    if request.method =="POST":
        
        password.delete()
        return redirect("index")
    return render(request,"main/delete.html",{'password':password})